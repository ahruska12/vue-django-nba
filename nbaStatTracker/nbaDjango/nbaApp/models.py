from django.db import models
from django.utils import timezone


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    conference = models.CharField(max_length=50)
    division = models.CharField(max_length=50)
    wins = models.IntegerField()
    losses = models.IntegerField()
    team_ppg = models.CharField(max_length=50)
    team_rpg = models.CharField(max_length=50)
    team_apg = models.CharField(max_length=50)
    opp_ppg = models.CharField(max_length=50)

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
