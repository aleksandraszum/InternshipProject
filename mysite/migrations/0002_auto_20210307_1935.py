# Generated by Django 3.1.7 on 2021-03-07 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='note',
            index_together={('note_uuid', 'version')},
        ),
    ]
