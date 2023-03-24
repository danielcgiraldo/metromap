from django.urls import path
from .views import tweets

urlpatterns = [
    path("v1/tweets/", tweets),
]
