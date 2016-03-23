from django.contrib.auth.models import User, Group
from .models import Team, Club, Player, SensorReading
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups', 'club')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'url', 'name', 'user', 'members', 'teams')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'url', 'name', 'club', 'players')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'url', 'first_name', 'last_name', 'team', 'club', 'position')


class SensorReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorReading
        fields = ('id', 'url', 'rssi', 'mac_address', 'timestamp', 'receiver', 'distance')


