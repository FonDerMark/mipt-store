# Generated by Django 4.0.3 on 2022-08-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_notebook_photo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='photo_name',
            field=models.CharField(max_length=50),
        ),
    ]
