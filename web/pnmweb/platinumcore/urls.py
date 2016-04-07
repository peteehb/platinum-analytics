from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from views import *

urlpatterns = patterns(
    '',
    url(r'^accounts/login/$', login_user),
    url(r'^login/$', login_user, name="login"),
    url(r'^logout/$', logout_user, name="logout"),

    url(r'^club/$', club_overview, name="club"),
    url(r'^team/$', teams_overview, name="team"),
    url(r'^players/(?P<player_id>[\w\-]+)/$', player_overview, name="player"),
    url(r'^players/$', players_overview, name="players"),


    url(r'^sensor-reading/$', sensor_readings, name="reading"),
    url(r'^sensor-reading-filter/$', sensor_readings_filter, name='reading_filter'),

    url(r'^pitch/$', add_pitch, name='pitch'),
)

