# Generated by Django 3.0.8 on 2022-05-16 03:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0005_auto_20220515_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='Date_Line',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 16, 9, 55, 28, 539636)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='published_on',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 16, 9, 55, 28, 539636)),
        ),
    ]
