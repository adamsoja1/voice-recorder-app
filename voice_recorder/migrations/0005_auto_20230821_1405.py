# Generated by Django 3.2 on 2023-08-21 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_recorder', '0004_auto_20230821_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 8, 21, 14, 5, 56, 897738)),
        ),
        migrations.AlterField(
            model_name='recordgroup',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 8, 21, 14, 5, 56, 898292)),
        ),
    ]