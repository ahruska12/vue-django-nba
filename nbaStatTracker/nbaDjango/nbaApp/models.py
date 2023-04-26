from django.db import models
from django.utils import timezone


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=200, default=0)
    abbreviation = models.CharField(max_length=3, default=0)
    city = models.CharField(max_length=50, default=0)
    state = models.CharField(max_length=50, default=0)
    conference = models.CharField(max_length=50, default=0)
    division = models.CharField(max_length=50, default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    team_ppg = models.CharField(max_length=50, default=0)
    team_rpg = models.CharField(max_length=50, default=0)
    team_apg = models.CharField(max_length=50, default=0)
    opp_ppg = models.CharField(max_length=50, default=0)

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=100, default="null")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)


"""
class Game(models.Model):
    game_id = models.IntegerField(primary_key=True, default=0)
    date = models.CharField(default=0, max_length=50)
    time = models.CharField(default=0, max_length=50)
    home_team = models.ManyToManyField(Team)
    away_team = models.ManyToManyField(Team)
    channel = models.CharField(default=0, max_length=50)
"""