# Generated by Django 3.0.8 on 2022-05-16 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0007_auto_20220516_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='Date_Line',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 16, 11, 3, 7, 709555)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='published_on',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 16, 11, 3, 7, 709555)),
        ),
    ]
