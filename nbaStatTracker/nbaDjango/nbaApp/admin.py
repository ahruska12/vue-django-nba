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
                    )
    list_filter = ('name',
                   )
    search_fields = ('name',
                     )
    ordering = ['name']


admin.site.register(Team, TeamList)
admin.site.register(Player, PlayerList)
