# Generated by Django 4.0.3 on 2022-08-09 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField(max_length=20)),
                ('model', models.TextField(max_length=50)),
                ('diag', models.TextField(max_length=5)),
                ('processor', models.TextField(max_length=10)),
                ('memory', models.TextField(max_length=10)),
                ('disk_type', models.TextField(max_length=10)),
                ('disk_volume', models.TextField(max_length=10)),
            ],
        ),
    ]
