# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-03 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='find',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('m_id', models.IntegerField(null=True)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='trnx',
            name='loc_lat',
        ),
        migrations.RemoveField(
            model_name='trnx',
            name='loc_lon',
        ),
        migrations.RemoveField(
            model_name='trnx',
            name='user',
        ),
        migrations.AddField(
            model_name='mechanic',
            name='mlat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='mlon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='trnx',
            name='damage',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='trnx',
            name='mechid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trnx',
            name='usrid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='bike_engine',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='reg_id',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='rider',
            name='home_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='rider',
            name='home_lon',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='pin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trnx',
            name='time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='lon',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='pin',
            field=models.IntegerField(null=True),
        ),
    ]