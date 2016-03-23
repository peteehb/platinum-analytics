from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from forms import *
from django.contrib.auth.decorators import login_required
import requests

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


def sensor_readings(request):
    if request.method == 'GET':
        data_response = requests.get('http://127.0.0.1:8000/sensor-reading')
        if data_response.status_code == 200:
            data = data_response.json()['results']
            return render(request, 'dashboard.html', {'sensor_readings': data})

        return render(request, 'dashboard.html')
