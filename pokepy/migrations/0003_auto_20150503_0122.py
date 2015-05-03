# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokepy', '0002_auto_20150503_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='abilities',
            name='ability',
            field=models.TextField(default=b'default'),
        ),
        migrations.AddField(
            model_name='egggroups',
            name='egg_group',
            field=models.CharField(default=b'default', max_length=50),
        ),
        migrations.AddField(
            model_name='moves',
            name='move',
            field=models.TextField(default=b'default'),
        ),
        migrations.AddField(
            model_name='moves',
            name='type',
            field=models.TextField(default=b'default'),
        ),
        migrations.AddField(
            model_name='search',
            name='query_text',
            field=models.CharField(default=b'default', max_length=50),
        ),
    ]
