# load_nba_players/models.py

from django.db import models


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    birthdate = models.DateField()
    years_pro = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
