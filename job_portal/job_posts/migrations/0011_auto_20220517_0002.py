# Generated by Django 3.0.8 on 2022-05-16 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_posts', '0010_auto_20220516_2332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job_apply',
            options={'verbose_name_plural': 'Job Apply'},
        ),
        migrations.AddField(
            model_name='job_apply',
            name='Email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job_apply',
            name='Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job_apply',
            name='Apply_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 17, 0, 2, 17, 523953)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='Date_Line',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 17, 0, 2, 17, 522953)),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='published_on',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 17, 0, 2, 17, 522953)),
        ),
    ]
