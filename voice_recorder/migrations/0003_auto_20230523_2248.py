# Generated by Django 3.2 on 2023-05-23 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_recorder', '0002_auto_20230523_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 23, 22, 48, 1, 548698)),
        ),
        migrations.AlterField(
            model_name='recordgroup',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 23, 22, 48, 1, 549245)),
        ),
    ]
