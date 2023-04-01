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

for nba_player in nba_players:
    player = Player(name=nba_player['full_name']
                    )
    player.save()

"""This is the ideal function for getting player name & assigning a team to them however 
    it keeps timing out..."""
# for nba_player in nba_players:
#    player_info = commonplayerinfo.CommonPlayerInfo(player_id=nba_player['id'])
#    player_data = player_info.common_player_info.get_dict()['data']
#    # team = Team.objects.get(abbreviation=player_data['TEAM_ABBREVIATION'])
#    player = Player(name=player_data[0][3],
#                    team=player_data[0][20]
#                    )
#    player.save()
