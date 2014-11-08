# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_auto_20141108_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(serialize=False, primary_key=True)),
                ('phone_number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person2Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_id', models.IntegerField()),
                ('date', models.IntegerField()),
                ('date_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person2Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
