# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilities',
            name='ability',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AlterField(
            model_name='moves',
            name='move',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AlterField(
            model_name='moves',
            name='type',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='egg_group',
            field=models.CharField(default='default', max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='games',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(default='bob', max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type1',
            field=models.CharField(default='normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type2',
            field=models.CharField(default='normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='search',
            name='query_text',
            field=models.CharField(default='default', max_length=50),
        ),
    ]
