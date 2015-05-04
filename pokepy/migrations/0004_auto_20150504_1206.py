# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepy', '0003_auto_20150503_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilities',
            name='ability',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='egggroups',
            name='egg_group',
            field=models.CharField(max_length=50, default='default'),
        ),
        migrations.AlterField(
            model_name='moves',
            name='move',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='moves',
            name='type',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='egg_group',
            field=models.CharField(max_length=50, default='default'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='games',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=50, default='digimon'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(max_length=50, default='normal'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(max_length=50, default='normal'),
        ),
        migrations.AlterField(
            model_name='search',
            name='query_text',
            field=models.CharField(max_length=50, default='default'),
        ),
    ]
