# Generated by Django 3.0.8 on 2022-05-16 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20220516_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_seeker_profile',
            name='Location',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]