from django.contrib.auth.models import User, Group
import django_filters
from .models import Team, Club, Player, SensorReading, Pitch
from rest_framework import viewsets
from pagination import LargeResultsSetPagination, StandardResultsSetPagination
from serializers import UserSerializer, GroupSerializer, ClubSerializer, TeamSerializer, PlayerSerializer, \
    SensorReadingSerializer, PitchSerializer
from rest_framework import filters


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


class SensorReadingFilter(filters.FilterSet):
    time_start = django_filters.NumberFilter(name="timestamp", lookup_type='gte')
    time_end = django_filters.NumberFilter(name="timestamp", lookup_type='lte')
    node = django_filters.CharFilter(name="mac_address", lookup_type='iexact')

    class Meta:
        model = SensorReading
        fields = ['node', 'time_start', 'time_end', 'receiver', 'distance']


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = SensorReadingFilter


class PitchFilter(filters.FilterSet):
    query_name = django_filters.CharFilter(name="name", lookup_type='iexact')

    class Meta:
        model = Pitch
        fields = ['query_name']


class PitchViewSet(viewsets.ModelViewSet):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_class = PitchFilter
