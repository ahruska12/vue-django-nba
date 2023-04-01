from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


    def __str__(self):
        return str(self.name)


class Player(models.Model):
    name = models.CharField(max_length=100, default="null")
    team = models.CharField(max_length=50)
    #team = models.ForeignKey(Team, on_delete=models.CASCADE)

