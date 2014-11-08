# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0017_auto_20141108_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={},
        ),
        migrations.RemoveField(
            model_name='people',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='people',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=-1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people',
            name='user',
            field=models.OneToOneField(default=-1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
