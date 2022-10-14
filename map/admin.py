from django.contrib.gis.admin import OSMGeoAdmin, register
from .models import Location, Category


@register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'coordinate')


@register(Category)
class CategoryAdmin(OSMGeoAdmin):
    list_display = ('id', 'name')
