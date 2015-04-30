# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abilities',
            name='pokemon',
        ),
        migrations.RemoveField(
            model_name='moves',
            name='pokemon',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='abilities',
            field=models.ManyToManyField(to='pokepy.abilities'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(to='pokepy.moves'),
        ),
    ]
