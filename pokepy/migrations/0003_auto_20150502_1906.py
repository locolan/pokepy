# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepy', '0002_auto_20150502_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='EggGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='abilities',
            name='ability',
        ),
        migrations.RemoveField(
            model_name='moves',
            name='move',
        ),
        migrations.RemoveField(
            model_name='moves',
            name='type',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='abilities',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='description',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='egg_group',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='games',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='moves',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='name',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='type1',
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='type2',
        ),
        migrations.RemoveField(
            model_name='search',
            name='query_text',
        ),
    ]
