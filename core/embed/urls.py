from django.urls import path
from .views import tweets

# Añadimos la vista tweets a las urls
urlpatterns = [
    path("v1/tweets/", tweets),
]
