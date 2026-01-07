from django.contrib import admin
from django.urls import path, include  # 1. Agrega 'include' aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_Farmacia.urls')),  # 2. Agrega esta línea para conectar tu app
]