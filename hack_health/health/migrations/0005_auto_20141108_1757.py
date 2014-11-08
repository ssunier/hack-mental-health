# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_person_person2day_person2person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='mood_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
