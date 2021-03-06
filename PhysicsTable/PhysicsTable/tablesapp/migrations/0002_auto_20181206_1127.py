# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-06 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Energy_Level_4_Trivalent_Lanthanides_in_various_Media_in_cm_Inverse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matrix', models.CharField(max_length=500)),
                ('E1', models.FloatField()),
                ('E2', models.FloatField()),
                ('E3', models.FloatField()),
                ('I4f', models.FloatField()),
                ('Alpha', models.FloatField()),
                ('Beta', models.FloatField()),
                ('Gama', models.FloatField()),
                ('NoOf_levels_fit', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Nd3Plus_in_LaCl3__Nd3Plus_in_LaF3',
            new_name='Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3',
        ),
    ]
