from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'sensor-readings', views.SensorReadingViewSet)
router.register(r'pitches', views.PitchViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^rest-auth/', include('rest_auth.urls'))
]
