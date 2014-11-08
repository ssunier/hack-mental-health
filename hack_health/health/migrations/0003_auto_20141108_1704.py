# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20141108_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='mood_id',
            field=models.ForeignKey(to='health.Mood'),
        ),
    ]
