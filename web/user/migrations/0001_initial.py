# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.URLField(blank=True, null=True)),
                ('second', models.URLField(blank=True, null=True)),
                ('third', models.URLField(blank=True, null=True)),
                ('fourth', models.URLField(blank=True, null=True)),
                ('fifth', models.URLField(blank=True, null=True)),
                ('sixth', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32, verbose_name='目标城市')),
                ('min_distance', models.FloatField(default=1.0, verbose_name='最小查找范围')),
                ('max_distance', models.FloatField(default=50.0, verbose_name='最大查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_dating_age', models.IntegerField(default=50, verbose_name='最大交友年龄')),
                ('dating_sex', models.CharField(choices=[('Male', '男性'), ('Female', '女性'), ('All', '不限')], max_length=16, verbose_name='匹配的性别')),
                ('vibration', models.BooleanField(default=True, verbose_name='开启震动')),
                ('only_matche', models.BooleanField(default=False, verbose_name='不让为匹配的人看我的相册')),
                ('auto_play', models.BooleanField(default=False, verbose_name='自动播放视频')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=16, unique=True)),
                ('nickname', models.CharField(max_length=16)),
                ('sex', models.CharField(choices=[('Male', '男'), ('Female', '女')], max_length=16)),
                ('birth_year', models.IntegerField(default=1990)),
                ('birth_month', models.IntegerField(default=1)),
                ('birth_day', models.IntegerField(default=1)),
                ('location', models.CharField(max_length=32, verbose_name='常居地')),
                ('vip_id', models.IntegerField()),
                ('vip_expiration', models.DateTimeField(auto_now_add=True, verbose_name='会员过期时间')),
            ],
        ),
    ]
