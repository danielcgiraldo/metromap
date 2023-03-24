from django.urls import path
from .views import HolaMundo, tweets

urlpatterns = [
    path("v1/tweets/", tweets),
]
