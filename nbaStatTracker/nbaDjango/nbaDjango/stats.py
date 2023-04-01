import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbaDjango.settings")
import django

django.setup()

# script

from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import commonplayerinfo
from nbaApp.models import Team, Player

# get list of all teams and info

# nba_teams = teams.get_teams()

# get nba teams into local database

# for nba_team in nba_teams:
#    team = Team(name=nba_team['full_name'],
#                abbreviation=nba_team['abbreviation'],
#               city=nba_team['city'],
#                state=nba_team['state']
#               )
#    team.save()

# get list of all players and info

# all_players = commonallplayers.CommonAllPlayers(is_only_current_season=1)
# all_players_data = all_players.get_data_frames()[0]
nba_players = players.get_active_players()
# get players into database

for nba_player in nba_players:
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player['id'])
    player_data = player_info.common_player_info.get_data_frame()
    #team = Team.objects.get(abbreviation=player_data['TEAM_ABBREVIATION'])
    player = Player(name=player_data['DISPLAY_FIRST_LAST'],
                    team=player_data['TEAM_NAME']
                    )
    player.save()

