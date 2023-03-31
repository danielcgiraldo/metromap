from django.urls import path
from .views import map

# Añadimos la vista tweets a las urls
urlpatterns = [
    path("v1/map/", map),
]
