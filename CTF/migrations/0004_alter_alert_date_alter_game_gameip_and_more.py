# Generated by Django 4.1.2 on 2022-10-17 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTF', '0003_alter_alert_date_alter_game_gameid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 16, 33, 50, 157629)),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameIP',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='gamePort',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 17, 16, 33, 50, 153630)),
        ),
    ]
