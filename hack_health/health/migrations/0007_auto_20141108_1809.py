# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_mood_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mood',
            name='name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
