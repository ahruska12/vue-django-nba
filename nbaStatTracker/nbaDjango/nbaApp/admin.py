from django.contrib import admin
from .models import Team, Player


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
                    'team',
                    )
    list_filter = ('name',
                   'team',
                   )
    search_fields = ('name',
                     'team',
                     )
    ordering = ['team']


admin.site.register(Team, TeamList)
admin.site.register(Player, PlayerList)
