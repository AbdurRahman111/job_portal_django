# Generated by Django 3.0.8 on 2022-05-16 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220516_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 16, 10, 4, 9, 678869)),
        ),
        migrations.AlterField(
            model_name='newsletter_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 16, 10, 4, 9, 679866)),
        ),
    ]
