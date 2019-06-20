from django.urls import path
from .views import SupplierAllView,SupplierDetailView,SupplierLocationView,SupplierFavoriteView


urlpatterns = [
    path('/', SupplierAllView.as_view()),
    path('/<int:pk>', SupplierDetailView.as_view()),
    path('/location', SupplierLocationView.as_view()),
    path('/<int:pk>/favorite', SupplierFavoriteView.as_view()),
    ]