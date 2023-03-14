import numpy as np
import requests
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playergamelog
from django.http import JsonResponse


def get_player_stats(player_id):
    # Use the NBA Python API to retrieve the player's stats
    # You will need to install the nba_api package first
    # player_info = commonplayerinfo.CommonPlayerInfo(player_name).get_dict()['resultSets'][0]['rowSet'][0]
    # player_id = player_info[0]
    # player_career_stats = \
    # playercareerstats.PlayerCareerStats(player_id=player_id).get_dict()['resultSets'][0]['rowSet'][0]
    career = playergamelog.PlayerGameLog(player_id=player_id, season='2022-23')
    df = career.get_data_frames()[0]
    total_points = df['PTS'].sum()
    total_assists = 0
    total_rebounds = 0
    player_stat_get = {
        'points_per_game': total_points,
        'assists_per_game': total_assists,
        'rebounds_per_game': total_rebounds,
    }
    return player_stat_get


def player_stats(player_name):
    # Call the get_player_stats function to retrieve the player's stats
    player_stats_request = get_player_stats(player_name)
    # Convert any int64 objects to regular int objects
    player_stats_request = convert_int64_to_int(player_stats_request)
    # Return the stats as a JSON response
    return JsonResponse(player_stats_request)


def convert_int64_to_int(data):
    # Recursively convert int64 objects to int objects in a dictionary or list
    if isinstance(data, dict):
        return {convert_int64_to_int(key): convert_int64_to_int(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_int64_to_int(item) for item in data]
    elif isinstance(data, np.int64):
        return int(data)
    else:
        return data


def getPlayerGamelog(player_id):
    career = playergamelog.PlayerGameLog(player_id=player_id, season='2022-23')
    df = career.get_data_frames()[0]
    return df


player = player_stats(203999)

print(player)
