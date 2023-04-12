from django.urls import path
from api import views
from api.controllers.auth_controller import secret_authentication

urlpatterns = [
    #All API endpoints
    path('v1/status/', lambda request: secret_authentication(views.get_status, request, 1)),
    path('v1/status/<slug:line>', views.get_status_line),
    path('v1/status/<slug:line>/<slug:station>', views.get_status_station),
    path('v1/data/', views.get_data),
    path('v1/data/<slug:line>', views.get_data_line),
    path('v1/data/<slug:line>/<slug:station>', views.get_data_station),
    path('v1/incident/', views.get_data),
    path('v1/incident/<slug:line>', views.get_data_line),
    path('v1/incident/<slug:line>/<slug:station>', views.get_data_station)
]

    