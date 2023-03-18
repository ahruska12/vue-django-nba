import numpy as np
import requests
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playergamelog
from nba_api.stats.library.data import players
from django.http import JsonResponse
import math


def roundup(number):
    rounded_num = math.ceil(number * 100) / 100
    return rounded_num


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
    average_points = df['PTS'].mean()
    average_points = roundup(average_points)
    total_assists = df['REB'].sum()
    average_assists = df['REB'].mean()
    average_assists = roundup(average_assists)
    total_rebounds = df['AST'].sum()
    average_rebounds = df['AST'].mean()
    average_rebounds = roundup(average_rebounds)
    total_minutes = df['MIN'].sum()
    average_minutes = df['MIN'].mean()
    total_fg = df['FGA'].sum()
    fg_Percent = df['FG_PCT']
    total_fg3 = df['FG3M'].sum()
    fg3_percent = df['FG3_PCT']
    total_freeThrow = df['FTM'].sum()
    freeThrow_percent = df['FT_PCT'].sum()
    offense_rebound = df['OREB'].sum()
    average_oReb = df['OREB'].mean()
    average_oReb = roundup(average_oReb)
    defense_rebound = df['DREB'].sum()
    average_dreb = df['DREB'].mean()
    average_dreb = roundup(average_dreb)
    total_steal = df['STL'].sum()
    average_steal = df['STL'].mean()
    average_steal = roundup(average_steal)
    total_block = df['BLK'].sum()
    average_block = df['BLK'].mean()
    average_block = roundup(average_block)
    total_turn = df['TOV'].sum()
    average_turn = df['TOV'].mean()
    average_turn = roundup(average_turn)
    total_foul = df['PF'].sum()
    average_foul = df['PF'].mean()
    average_foul = roundup(average_foul)

    player_stat_get = {
        'average_points': average_points,
        'total_points': total_points,
        'average_assists': average_assists,
        'total_assists': total_assists,
        'average_rebounds': average_rebounds,
        'total_rebounds': total_rebounds,
        'total_minutes': total_minutes,
        'average_minutes': average_minutes,
        'total_fg': total_fg,
        'fg_Percent': fg_Percent,
        'total_fg3': total_fg3,
        'fg3_percent': fg3_percent,
        'total_freeThrow': total_freeThrow,
        'freeThrow_percent': freeThrow_percent,
        'offense_rebound': offense_rebound,
        'average_oReb': average_oReb,
        'defense_rebound': defense_rebound,
        'average_dreb': average_dreb,
        'total_steal': total_steal,
        'average_steal': average_steal,
        'total_block': total_block,
        'average_block': average_block,
        'total_turn': total_turn,
        'average_turn': average_turn,
        'total_foul': total_foul,
        'average_foul': average_foul,
    }
    return player_stat_get

player_id = 203999
player = get_player_stats(player_id)

print(player['total_minutes'])
