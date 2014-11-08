# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0013_auto_20141108_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 8, 22, 26, 6, 99204, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='day',
            name='weather_id',
            field=models.ForeignKey(to='health.Weather'),
        ),
    ]
