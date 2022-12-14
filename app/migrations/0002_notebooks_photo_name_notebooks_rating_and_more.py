# Generated by Django 4.0.3 on 2022-08-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebooks',
            name='photo_name',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='notebooks',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='brand',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='diag',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='disk_type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='disk_volume',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='memory',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='processor',
            field=models.CharField(max_length=10),
        ),
    ]
