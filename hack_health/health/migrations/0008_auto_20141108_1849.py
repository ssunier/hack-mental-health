# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0007_auto_20141108_1809'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person2Day',
        ),
        migrations.DeleteModel(
            name='Person2Person',
        ),
    ]
