# Generated by Django 3.0.8 on 2022-05-15 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220515_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Subject', models.CharField(max_length=255)),
                ('Message', models.CharField(max_length=255)),
                ('Time', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 15, 21, 17, 39, 812693))),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
    ]
