from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from nbaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.team_list),
    url(r'^api/teams/$', views.team_list),
    url(r'^api/teams/(?P<pk>[0-9]+)$', views.getTeam),
    path('players/', views.player_list),
    url(r'^api/players/$', views.player_list),
    url(r'^api/players/(?P<pk>[0-9]+)$', views.getPlayer),
    path('register/', views.RegisterView.as_view(), name='auth_register'), ]

# username - admin
# password - adminpassword
