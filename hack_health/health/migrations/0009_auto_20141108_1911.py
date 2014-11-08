# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_auto_20141108_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person2Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.IntegerField()),
                ('date_id', models.ForeignKey(to='health.Day')),
                ('person_id', models.ForeignKey(to='health.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='contact_name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='contact_number',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
