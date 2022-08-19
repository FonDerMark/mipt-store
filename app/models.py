from django.contrib.auth.models import User
from django.db import models


class Notebook(models.Model):
    product = 'Ноутбук'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    diag = models.CharField(max_length=5)
    processor = models.CharField(max_length=10)
    memory = models.CharField(max_length=10)
    disk_type = models.CharField(max_length=10)
    disk_volume = models.CharField(max_length=10)
    photo_path = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    articl = models.IntegerField(default=0)


class Smartphone(models.Model):
    product = 'Смартфон'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    diag = models.CharField(max_length=5)
    processor = models.CharField(max_length=10)
    memory = models.CharField(max_length=10)
    disk_volume = models.CharField(max_length=10)
    photo_path = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    articl = models.IntegerField(default=0)


class TV(models.Model):
    product = 'Телевизор'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    diag = models.CharField(max_length=5)
    smart = models.BooleanField()
    photo_path = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    articl = models.IntegerField(default=0)


class Cleaners(models.Model):
    product = 'Стиральная машина'
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    power = models.CharField(max_length=5)
    num_of_programms = models.CharField(max_length=10)
    volume = models.CharField(max_length=10)
    dry = models.BooleanField(default=False)
    photo_path = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    articl = models.IntegerField(default=0)


class ToCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    articl = models.IntegerField()
