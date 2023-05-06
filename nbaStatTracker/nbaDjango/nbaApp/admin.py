from django.contrib import admin
from .models import Team, Player, Favorite


class TeamList(admin.ModelAdmin):
    list_display = ('name',
                    'abbreviation',
                    'city',
                    'state',
                    )
    list_filter = (
        'state',
    )
    search_fields = ('name',
                     'abbreviation',
                     'city',
                     'state',
                     )
    ordering = ['name']


class PlayerList(admin.ModelAdmin):
    list_display = ('name',
                    'team'
                    )
    list_filter = ('team',
                   'points')

    search_fields = ('name',
                     'team',
                     'points',
                     'rebounds',
                     'assists',
                     'steals',
                     'blocks',
                     'games_played',
                     )
    ordering = ['name']

class FavoriteList(admin.ModelAdmin):
    list_filter = ('team',
                   'player')
    search_fields = ('team',
                     'player')
    ordering = ['player']



admin.site.register(Team, TeamList)
admin.site.register(Player, PlayerList)
admin.site.register(Favorite, FavoriteList)
