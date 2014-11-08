# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('date_id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mood_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='mood',
            name='id',
        ),
        migrations.AddField(
            model_name='mood',
            name='mood_id',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
