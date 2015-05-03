# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='abilities',
            field=models.ManyToManyField(to='pokepy.Abilities'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default=b'default'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='egg_group',
            field=models.CharField(default=b'default', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='games',
            field=models.TextField(default=b'default'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(to='pokepy.Moves'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='name',
            field=models.CharField(default=b'digimon', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(default=b'normal', max_length=50),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(default=b'normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
