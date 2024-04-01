from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', include('companies.urls')), # Add companies app urls.py
    path('employees/', include('employees.urls')), # Add employees app urls.py
    path('devices/', include('devices.urls')), # Add devices app urls.py
]
