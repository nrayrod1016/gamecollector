# Generated by Django 3.2.4 on 2021-09-06 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210905_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playing',
            old_name='meal',
            new_name='play',
        ),
    ]
