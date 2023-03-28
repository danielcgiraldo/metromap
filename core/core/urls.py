from django.contrib import admin
from django.urls import path, include

# Incluimos las urls de embed y de la api a la aplicación
urlpatterns = [
    path("", include("embed.urls")),
    path("", include("api.urls")),
    path("admin/", admin.site.urls),
]