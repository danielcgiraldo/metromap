from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    #URL donde se entrega el json de los tweets
    path('v1/tweets/', views.get_tweets_endpoint),
]

    