# Generated by Django 3.2 on 2023-05-23 18:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RecordGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=datetime.datetime(2023, 5, 23, 18, 50, 45, 52266))),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=datetime.datetime(2023, 5, 23, 18, 50, 45, 51829))),
                ('audio_file', models.FileField(upload_to='records/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice_recorder.author')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voice_recorder.recordgroup')),
            ],
        ),
    ]
