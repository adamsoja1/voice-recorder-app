# Generated by Django 3.2 on 2023-08-18 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_recorder', '0002_auto_20230818_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 8, 18, 23, 14, 27, 19234)),
        ),
        migrations.AlterField(
            model_name='recordgroup',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 8, 18, 23, 14, 27, 19601)),
        ),
    ]