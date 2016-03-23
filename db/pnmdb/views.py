from django.contrib.auth.models import User, Group
import bluetooth_utils as utils
from .models import Team, Club, Player, SensorReading
from rest_framework import viewsets
from pagination import LargeResultsSetPagination, StandardResultsSetPagination
from serializers import UserSerializer, GroupSerializer, ClubSerializer, TeamSerializer, PlayerSerializer, \
    SensorReadingSerializer
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClubViewSet(viewsets.ModelViewSet):
    """Club endpoint
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """Teams endpoint
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """Players endpoint
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    pagination_class = LargeResultsSetPagination

    # def create(self, request, *args, **kwargs):
    #     data = self.prepare_data(request.data)
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def prepare_data(self, data):
    #     rssi = data['rssi']
    #     rssi_val = utils.rssi_to_integer(rssi)
    #     data['distance'] = utils.rssi_to_meters(rssi_val)
    #     return data
