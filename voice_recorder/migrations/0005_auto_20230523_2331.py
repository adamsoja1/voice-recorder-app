# Generated by Django 3.2 on 2023-05-23 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_recorder', '0004_auto_20230523_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 23, 23, 31, 54, 291288)),
        ),
        migrations.AlterField(
            model_name='recordgroup',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 5, 23, 23, 31, 54, 291680)),
        ),
    ]