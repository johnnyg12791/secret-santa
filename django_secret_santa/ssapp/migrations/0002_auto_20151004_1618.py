# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='name',
            new_name='family_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=b'NoName', max_length=100),
        ),
    ]
