# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0005_alter_user_last_login_null'),
        ('health', '0010_auto_20141108_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.IntegerField()),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 8, 20, 44, 27, 263024, tzinfo=utc)),
        ),
    ]
