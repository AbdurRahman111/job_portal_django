# Generated by Django 3.0.8 on 2022-05-15 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=255)),
                ('Time', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 15, 21, 28, 50, 87817))),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
        migrations.AlterField(
            model_name='contact_table',
            name='Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 15, 21, 28, 50, 86590)),
        ),
    ]
