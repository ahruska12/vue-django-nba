from django.urls import path
from .getPlayer import get_player_stats
urlpatterns = [
    path('players/<str:player_id>/', get_player_stats),
    # other URL patterns here...
]
