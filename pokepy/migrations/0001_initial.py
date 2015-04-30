# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ability', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='egg_groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('egg_group', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='moves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('move', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type1', models.CharField(max_length=50)),
                ('type2', models.CharField(max_length=50)),
                ('games', models.TextField()),
                ('description', models.TextField()),
                ('egg_group', models.ForeignKey(to='pokepy.egg_groups')),
            ],
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('query_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='moves',
            name='pokemon',
            field=models.ManyToManyField(to='pokepy.pokemon'),
        ),
        migrations.AddField(
            model_name='abilities',
            name='pokemon',
            field=models.ManyToManyField(to='pokepy.pokemon'),
        ),
    ]
