# Generated by Django 3.0.8 on 2022-05-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220515_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_provider_profile',
            name='company_logo',
            field=models.FileField(blank=True, null=True, upload_to='job_provider/company_logo/'),
        ),
    ]