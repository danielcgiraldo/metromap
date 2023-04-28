from django.urls import path
from .views import map, check_incoming, get_data, get_incidents, get_update

# Map and API endpoints map uses.
# Endpoints work using api.metromap.online requests.
urlpatterns = [
    path("v1/map/", map),
    path("/api/v1/incident/<str:line>/<str:station>/", lambda request,
         line, station: check_incoming(request, get_incidents, line, station)),
    path("/api/v1/data/<str:line>/<str:station>/", lambda request, line,
         station: check_incoming(request, get_data, line, station)),
    path("/api/v1/update/", lambda request: check_incoming(request, get_update))
]