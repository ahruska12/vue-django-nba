from django.apps import AppConfig
from django.conf import settings
import os
from nba_api.stats.endpoints import commonallplayers
from load_nba_players.models import Player


class LoadNbaPlayersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'load_nba_players'

    # load_nba_players/apps.py

    def ready(self):
        # Check if there are any players in the database already
        if Player.objects.count() == 0:
            # Query the NBA API for all active players
            players = commonallplayers.CommonAllPlayers(is_only_current_season=1)
            players_dict = players.get_normalized_dict()['LeagueStandardPlayer']

            # Load each player's data into the Django database
            for player_data in players_dict:
                Player.objects.create(
                    player_id=player_data['PERSON_ID'],
                    first_name=player_data['FIRST_NAME'],
                    last_name=player_data['LAST_NAME'],
                    team=player_data['TEAM_CITY'] + ' ' + player_data['TEAM_NAME'],
                    position=player_data['POSITION'],
                    height=player_data['HEIGHT'],
                    weight=player_data['WEIGHT'],
                    birthdate=player_data['BIRTHDATE'],
                    years_pro=player_data['YEARS_PRO']
                )

            print('NBA players loaded successfully.')
