# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0004_pitch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='description',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
    ]
