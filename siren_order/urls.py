from django.urls import include, path
from django.contrib import admin
import debug_toolbar


urlpatterns = [
    path('supplier', include('supplier.urls')),
    path('product', include('product.urls')),    
    path('user', include('user.urls')),
    path('order', include('order.urls')),
    path('admin/', admin.site.urls),
]