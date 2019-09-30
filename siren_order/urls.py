from django.urls import include, path
from django.contrib import admin
import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('supplier', include('supplier.urls')),
    path('product', include('product.urls')),    
    path('user', include('user.urls')),
    path('order', include('order.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
