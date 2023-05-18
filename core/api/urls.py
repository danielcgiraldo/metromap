from django.urls import path
from api import views
from api.controllers.auth_controller import secret_authentication
urlpatterns = [
    #All API endpoints
    path('v1/status/', lambda request: secret_authentication(views.get_status, request, 1)),
    path('v1/status/<slug:line>', lambda request, line: secret_authentication(views.get_status, request, 0.8, line)),
    path('v1/status/<slug:line>/<slug:station>', lambda request, line, station: secret_authentication(views.get_status, request, 0.5, line, station)),

    path('v1/data/', lambda request: secret_authentication(views.get_data, request, 1)),
    path('v1/data/<slug:line>', lambda request, line: secret_authentication(views.get_data, request, 0.7, line)),
    path('v1/data/<slug:line>/<slug:station>', lambda request, line, station: secret_authentication(views.get_data, request, 0.5, line, station)),

    path('v1/incident/', lambda request: secret_authentication(views.get_incident, request, 1.5)),
    path('v1/incident/<slug:line>', lambda request, line: secret_authentication(views.get_incident, request, 1, line)),
    path('v1/incident/<slug:line>/<slug:station>', lambda request, line, station: secret_authentication(views.get_incident, request, 0.8, line, station)),
    
    path("v1/user/<slug:type>/<str:id>", lambda request, type, id: views.user(request, type, id)),
]
