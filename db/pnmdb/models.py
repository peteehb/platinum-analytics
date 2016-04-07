from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class Team(models.Model):
    club = models.ForeignKey(Club, related_name='teams', null=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return "%s" % self.name


class Player(models.Model):
    team = models.ManyToManyField(Team, related_name='players')
    club = models.ForeignKey(Club, related_name='members', null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    POSITION_CHOICES = (
        ('Goalkeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Forward', 'Forward')
    )
    position = models.CharField(max_length=64, choices=POSITION_CHOICES)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class SensorReading(models.Model):
    rssi = models.CharField(max_length=32)
    mac_address = models.CharField(max_length=64)
    timestamp = models.CharField(max_length=64)
    receiver = models.IntegerField()
    distance = models.FloatField()


class Pitch(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256)
    width = models.IntegerField()
    length = models.IntegerField()
