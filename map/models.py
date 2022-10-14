from django.contrib.gis.db import models
from core.settings import PROJECT_ROOT


class Category(models.Model):
    name = models.CharField(max_length=255)


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255, null=True, blank=True)
    long = models.CharField(max_length=255, null=True, blank=True)
    coordinate = models.PointField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
