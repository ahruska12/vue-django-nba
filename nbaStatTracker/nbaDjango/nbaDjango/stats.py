import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbaDjango.settings")
import django

django.setup()

# script

from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo, playergamelog
from nbaApp.models import Team, Player
import json

# get list of all teams and info

nba_teams = teams.get_teams()

# get nba teams into local database

for nba_team in nba_teams:
    team = Team(name=nba_team['full_name'],
                abbreviation=nba_team['abbreviation'],
                city=nba_team['city'],
                state=nba_team['state']
                )
    team.save()

# get list of all players and info


nba_players = players.get_active_players()

# get players into database
# should be around 495 players, give or take a few
# as of right now it takes 50 minutes to run this script
x = 1
for nba_player in nba_players:
    try:
        # player_info is grabbing the player specific information
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player['id'])
        # gamelog will be used to gather all the player stats, this excludes player specific info
        game_log = playergamelog.PlayerGameLog(player_id=nba_player['id'], season='2022-23')
        # player_data is turning player_info into a readable dictionary
        player_data = player_info.common_player_info.get_dict()['data']
        # data is turning the player gamelog into a dataframe, in this case it is easier than a dictionary
        data = game_log.get_data_frames()[0]
    except json.decoder.JSONDecodeError as e:
        # this error I believe is when a spot in player_data is empty, not sure
        # why its happening, but it does
        print(f"Error decoding JSON data: {e}")
        continue
    try:
        # set the "team" variable to match the 3 letter team abbreviation found in player_data
        team = Team.objects.get(abbreviation=player_data[0][20])
        # this grabs the current player's stats for the season and sums them up, ideally we can
        # divide the number of points by the number of games played to get the average of each stat
        games_played = len(data)
        points = data['PTS'].sum()
        rebounds = data['REB'].sum()
        assists = data['AST'].sum()
        steals = data['STL'].sum()
        blocks = data['BLK'].sum()
        # creating the player object
        player = Player(name=player_data[0][3],
                        team=team,
                        points=points,
                        rebounds=rebounds,
                        assists=assists,
                        steals=steals,
                        blocks=blocks,
                        games_played=games_played)
        player.save()
        print(f"Player {x} Created")
        # ran into an issue where it was going too fast and kept timing out
        # needed to add a 5-second delay after each player, and it works
        time.sleep(5)
        x = x + 1
    except Team.DoesNotExist:
        # NBA api is very up-to-date, players get cut all the time and when they do,
        # they don't have a team assigned so for those players they need to be taken out
        print(f"Skipping player {player_data[0][3]}")

# assigning stats to specific players
