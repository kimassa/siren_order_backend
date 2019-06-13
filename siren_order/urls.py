from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('supplier', include('supplier.urls')),
    path('admin/', admin.site.urls)
]