# Generated by Django 4.1.2 on 2022-10-11 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 10, 11, 13, 18, 36, 145660))),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='timeCreate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 11, 13, 18, 36, 145660)),
        ),
    ]
