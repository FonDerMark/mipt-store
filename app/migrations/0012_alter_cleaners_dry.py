# Generated by Django 4.0.3 on 2022-08-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_cleaners_smartphone_tv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaners',
            name='dry',
            field=models.BooleanField(default=False),
        ),
    ]
