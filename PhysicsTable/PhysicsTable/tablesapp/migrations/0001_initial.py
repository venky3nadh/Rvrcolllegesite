# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-17 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nd3Plus_in_LaCl3__Nd3Plus_in_LaF3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name1', models.CharField(max_length=500)),
                ('column_name2', models.CharField(max_length=500)),
                ('SLJ', models.CharField(max_length=500)),
                ('v_cm_Inverse_liqHe_a', models.CharField(max_length=500)),
                ('v_cm_Inverse_b1', models.IntegerField()),
                ('v_cm_Inverse_liqHe_c', models.CharField(max_length=500)),
                ('v_cm_Inverse_b2', models.IntegerField()),
                ('field_name1', models.CharField(max_length=500)),
                ('field_name2', models.CharField(max_length=500)),
                ('field_name3', models.CharField(max_length=500)),
                ('field_name4', models.CharField(max_length=500)),
            ],
        ),
    ]
