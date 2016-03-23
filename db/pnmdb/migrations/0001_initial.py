# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64, choices=[(b'Goalkeeper', b'Goalkeeper'), (b'Defender', b'Defender'), (b'Midfielder', b'Midfielder'), (b'Forward', b'Forward')])),
                ('club', models.ForeignKey(related_name='members', to='pnmdb.Club', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorReading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rssi', models.CharField(max_length=32)),
                ('mac_address', models.CharField(max_length=64)),
                ('timestamp', models.CharField(max_length=64)),
                ('receiver', models.IntegerField()),
                ('distance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('club', models.ForeignKey(related_name='teams', to='pnmdb.Club', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ManyToManyField(related_name='players', to='pnmdb.Team'),
        ),
    ]
