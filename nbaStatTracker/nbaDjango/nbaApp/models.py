from django.contrib.auth.models import User
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

    def __str__(self):
        return self.name


class Comparison(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_comparisons', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_comparisons', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    team1_value = models.DecimalField(max_digits=10, decimal_places=2)
    team2_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} - {self.category}"


class FavoriteTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, related_name='favorites')

    def __str__(self):
        return str(self.user)

class FavoritePlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    player = models.ManyToManyField(Player, related_name='favorites')

    def __str__(self):
        return str(self.user)



