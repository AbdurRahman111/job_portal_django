# Generated by Django 3.0.8 on 2022-05-18 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0011_auto_20220517_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_apply',
            name='Apply_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 18, 21, 50, 47, 786065)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='Date_Line',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 18, 21, 50, 47, 784046)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='published_on',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 18, 21, 50, 47, 784046)),
        ),
    ]
