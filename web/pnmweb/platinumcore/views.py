import urllib
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import time
from forms import *
from django.contrib.auth.decorators import login_required
import requests
from platinum.settings import PNMDB_URL


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "dashboard.html", {"user": user})
            else:
                return render(request, "login.html")
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return render(request, "login.html")


@login_required()
def club_overview(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClubForm()
    return render(request, 'club.html',
                  {'form': form})


@login_required()
def player_overview(request, player_id):
    player = Player.objects.all().filter(id=player_id)[0]
    return render(request, 'player.html',
                  {'player': player})


@login_required()
def teams_overview(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeamForm()
    return render(request, 'team.html',
                  {'form': form})


@login_required()
def players_overview(request):
    players = Player.objects.all()
    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            form = PlayerForm()

    return render(request, 'players.html',
                  {'players': players, 'form': form})


def sensor_readings(request, url):
    pnmdb_sensor_readings = PNMDB_URL + '/sensor-reading/?'

    data = []
    if request.method == 'GET':
        r = requests.get(pnmdb_sensor_readings)

        while r.json()['next'] is not None:
            if r.status_code == 200:
                data.append([reading for reading in r.json()['results']])
            r = requests.get(r.json()['next'])

        return render(request, 'dashboard.html', {'sensor_readings': data})

    return render(request, 'dashboard.html')


def sensor_readings_filter(request):
    if request.method == 'POST':
        form = SensorReadingFilterForm(request.POST)
        if form.is_valid():
            time_start = form.cleaned_data.get('time_start')
            time_start_timestamp = int(time.mktime(time_start.timetuple()) * 100)

            time_end = form.cleaned_data.get('time_end')
            time_end_timestamp = int(time.mktime(time_end.timetuple()) * 100)

            node = form.cleaned_data.get('node')
            url = PNMDB_URL + "/sensor-reading/?time_start={0}&time_end={1}&node={2}"\
                .format(time_start_timestamp, time_end_timestamp, node)
            import ipdb; ipdb.set_trace(

            )
            return redirect(sensor_readings, url)
    else:
        form = SensorReadingFilterForm()
    return render(request, 'form.html', {'form': form})
