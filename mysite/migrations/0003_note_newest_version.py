# Generated by Django 3.1.7 on 2021-03-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210307_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='newest_version',
            field=models.BooleanField(default=True),
        ),
    ]
