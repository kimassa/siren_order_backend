from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from supplier.views import SupplierAllView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'supplier', SupplierAllView, basename='supplier')

urlpatterns = [
    path('product', include('product.urls')),
    path('user', include('user.urls')),
    path('order', include('order.urls')),
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls
