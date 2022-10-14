"""Markers view."""

import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Location


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Location.objects.all()))
        for obj in context["markers"]['features']:
            obj['properties']['image'] = "http://localhost:8002/images/" + obj['properties']['image']
        return context