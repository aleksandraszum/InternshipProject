# Generated by Django 3.1.7 on 2021-03-07 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_uuid', models.CharField(max_length=36)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('modified', models.DateTimeField(default=datetime.datetime.now)),
                ('version', models.PositiveIntegerField(default=1)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
