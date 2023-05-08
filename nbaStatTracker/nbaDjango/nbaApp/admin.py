from django.contrib import admin
from .models import Team, Player, FavoriteTeam, FavoritePlayer


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


class FavoriteTeamList(admin.ModelAdmin):
    list_filter = ['team']
    search_fields = ['team']
    ordering = ['team']


class FavoritePlayerList(admin.ModelAdmin):
    list_filter = ['player']
    search_fields = ['player']
    ordering = ['player']


admin.site.register(Team, TeamList)
admin.site.register(Player, PlayerList)
admin.site.register(FavoriteTeam, FavoriteTeamList)
admin.site.register(FavoritePlayer, FavoritePlayerList)
