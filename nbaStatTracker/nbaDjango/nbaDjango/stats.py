import os
import sys
import time
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbaDjango.settings")
import django

django.setup()

# script

from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo, playergamelog, teaminfocommon, scoreboardv2
from nbaApp.models import Team, Player
import json
import pandas as pd


# get list of all teams and info

nba_teams = teams.get_teams()

# get nba teams into local database

for nba_team in nba_teams:
    team_id = nba_team['id']
    name = nba_team['full_name']
    abbreviation = nba_team['abbreviation']
    city = nba_team['city']
    state = nba_team['state']
    team_info = teaminfocommon.TeamInfoCommon(team_id=nba_team['id']).get_dict()
    conference = team_info['resultSets'][0]['rowSet'][0][5]
    division = team_info['resultSets'][0]['rowSet'][0][6]
    wins = team_info['resultSets'][0]['rowSet'][0][9]
    losses = team_info['resultSets'][0]['rowSet'][0][10]
    team_ppg = team_info['resultSets'][1]['rowSet'][0][4]
    team_rpg = team_info['resultSets'][1]['rowSet'][0][6]
    team_apg = team_info['resultSets'][1]['rowSet'][0][8]
    opp_ppg = team_info['resultSets'][1]['rowSet'][0][10]
    team = Team(team_id=team_id,
                name=name,
                abbreviation=abbreviation,
                city=city,
                state=state,
                conference=conference,
                division=division,
                wins=wins,
                losses=losses,
                team_ppg=team_ppg,
                team_rpg=team_rpg,
                team_apg=team_apg,
                opp_ppg=opp_ppg
                )
    team.save()
    time.sleep(.5)
    print(f"{name} added")

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
        player_id = nba_player['id']
        games_played = len(data)
        points = data['PTS'].sum()
        rebounds = data['REB'].sum()
        assists = data['AST'].sum()
        steals = data['STL'].sum()
        blocks = data['BLK'].sum()
        # creating the player object
        player = Player(player_id=player_id,
                        name=player_data[0][3],
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
        time.sleep(1)
        x = x + 1
    except Team.DoesNotExist:
        # NBA api is very up-to-date, players get cut all the time and when they do,
        # they don't have a team assigned so for those players they need to be taken out
        print(f"Skipping player {player_data[0][3]}")

# gathering game matchups

"""


current_date = datetime.now().strftime('%m-%d-%Y')
matchups = scoreboardv2.ScoreboardV2(game_date=current_date)
time.sleep(1)
info = matchups.get_dict()
data = info['resultSets'][0]['rowSet']
x=0
while x < len(data):
    game_id = data[x][2]
    date = data[x][0]
    home_team = Team.objects.get(team_id=data[x][6])
    away_team = Team.objects.get(team_id=data[x][7])
    time = data[x][4]
    channel = data[x][11]

    game = Game(game_id=game_id,
                date=date,
                home_team=home_team,
                away_team=away_team,
                time=time,
                channel=channel)
    game.save()
    time.sleep(1)
    x = x + 1
    print(f"matchup {x} added")

"""







