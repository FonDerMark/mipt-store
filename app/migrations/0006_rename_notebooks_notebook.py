# Generated by Django 4.0.3 on 2022-08-16 03:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_notebooks_ordered_by'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notebooks',
            new_name='Notebook',
        ),
    ]