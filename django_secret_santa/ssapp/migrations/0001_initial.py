# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('gift_preference', models.CharField(max_length=200)),
                ('family', models.ForeignKey(to='ssapp.Family')),
            ],
        ),
        migrations.AddField(
            model_name='gifts',
            name='giftee',
            field=models.ForeignKey(related_name='receiver', to='ssapp.Person'),
        ),
        migrations.AddField(
            model_name='gifts',
            name='gifter',
            field=models.ForeignKey(related_name='giver', to='ssapp.Person'),
        ),
    ]
