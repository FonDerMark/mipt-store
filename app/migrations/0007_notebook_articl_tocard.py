# Generated by Django 4.0.3 on 2022-08-16 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_rename_notebooks_notebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='articl',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ToCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articl', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]