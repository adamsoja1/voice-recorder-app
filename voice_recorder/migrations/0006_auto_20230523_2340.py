# Generated by Django 3.2 on 2023-05-23 23:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_recorder', '0005_auto_20230523_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 23, 23, 40, 7, 599111)),
        ),
        migrations.AlterField(
            model_name='recordgroup',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 23, 23, 40, 7, 599585)),
        ),
    ]