from django.urls import path
from .views import map, check_incoming

# Map and API endpoints map uses.
# Endpoints work using api.metromap.online requests.
urlpatterns = [
    path("v1/map/", map),
    path("request", check_incoming)
]