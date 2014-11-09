# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_auto_20141108_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('weather_id', models.AutoField(serialize=False, primary_key=True)),
                ('temperature', models.IntegerField()),
                ('weather', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='day',
            name='weather_id',
            field=models.ForeignKey(default=-1, to='health.Weather'),
            preserve_default=True,
        ),
    ]
