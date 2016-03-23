# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnmdb', '0002_auto_20160317_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorreading',
            name='distance',
            field=models.FloatField(),
        ),
    ]
