from django.urls import path
from .views import SupplierAllView,SupplierDetailView,SupplierLocationView,SupplierFavoriteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', SupplierAllView, basename='supplier')

# urlpatterns = [
#     path('/', SupplierAllView),
#     path('/<int:pk>', SupplierDetailView.as_view()),
#     path('/location', SupplierLocationView.as_view()),
#     path('/<int:pk>/favorite', SupplierFavoriteView.as_view()),
#     ]

urlpatterns = router.urls