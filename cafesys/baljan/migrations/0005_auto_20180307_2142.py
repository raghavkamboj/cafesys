# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-07 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baljan', '0004_incomingcallfallback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomingcallfallback',
            options={'ordering': ('-priority', 'user__username'), 'verbose_name': 'Styrelsemedlem att ringa', 'verbose_name_plural': 'Uppringningslista jourtelefon'},
        ),
        migrations.AddField(
            model_name='profile',
            name='card_cache',
            field=models.BigIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
