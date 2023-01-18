# Generated by Django 4.1.5 on 2023-01-18 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('created_at', models.DateField(blank=True, default=datetime.datetime(2023, 1, 18, 18, 14, 49, 87908))),
            ],
        ),
    ]
