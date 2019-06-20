from django.urls import path
from .views import SupplierView,SupplierDetailView,SupplierLocationView


urlpatterns = [
    path('/', SupplierView.as_view()),
    path('/<int:pk>', SupplierDetailView.as_view()),
    path('/location', SupplierLocationView.as_view()),
    ]