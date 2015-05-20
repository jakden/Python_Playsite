# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hearthstone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardViewer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('mana', models.CharField(max_length=200)),
                ('card', models.CharField(max_length=200)),
                ('card_attack', models.CharField(max_length=200)),
                ('card_health', models.CharField(max_length=200)),
                ('card_class', models.CharField(max_length=200)),
                ('card_ability_1', models.CharField(max_length=200)),
                ('card_ability_2', models.CharField(max_length=200)),
                ('card_ability_3', models.CharField(max_length=200)),
                ('card_png', models.CharField(max_length=200)),
                ('card_flavor_text', models.CharField(max_length=200)),
            ],
        ),
    ]
