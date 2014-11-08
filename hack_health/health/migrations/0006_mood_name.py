# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20141108_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='mood',
            name='name',
            field=models.CharField(default=b'none', max_length=50),
            preserve_default=True,
        ),
    ]
