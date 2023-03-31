from django.urls import path
from api import views


urlpatterns = [
    #All API endpoints
    path('v1/status/', views.get_status),
    path('v1/status/<slug:line>', views.get_status_line),
    path('v1/status/<slug:line>/<slug:station>', views.get_status_station),
    path('v1/data/', views.get_data),
    path('v1/data/<slug:line>', views.get_data_line),
    path('v1/data/<slug:line>/<slug:station>', views.get_data_station),
    path('v1/incident/', views.get_data),
    path('v1/incident/<slug:line>', views.get_data_line),
    path('v1/incident/<slug:line>/<slug:station>', views.get_data_station)
]

    