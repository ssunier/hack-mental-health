# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_auto_20141109_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 13, 20, 47, 224754, tzinfo=utc)),
        ),
    ]
