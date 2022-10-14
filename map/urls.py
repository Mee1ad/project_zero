from django.urls import path

from .views import MarkersMapView

app_name = "map"

urlpatterns = [
    path("map/", MarkersMapView.as_view()),
]
