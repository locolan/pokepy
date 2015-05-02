# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ability', models.CharField(default=b'default', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('move', models.CharField(default=b'default', max_length=50)),
                ('type', models.CharField(default=b'default', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'bob', max_length=50)),
                ('type1', models.CharField(default=b'normal', max_length=50)),
                ('type2', models.CharField(default=b'normal', max_length=50)),
                ('games', models.TextField(default=b'default')),
                ('description', models.TextField(default=b'default')),
                ('egg_group', models.CharField(default=b'default', max_length=50)),
                ('abilities', models.ManyToManyField(to='pokepy.Abilities')),
                ('moves', models.ManyToManyField(to='pokepy.Moves')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_text', models.CharField(default=b'default', max_length=50)),
            ],
        ),
    ]
