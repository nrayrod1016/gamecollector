# Generated by Django 3.2.4 on 2021-09-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_playing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playing',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='playing',
            name='date',
            field=models.DateField(verbose_name='Playing Date'),
        ),
    ]