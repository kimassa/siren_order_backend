from django.urls import path
from .views import SupplierView,SupplierLocationView


urlpatterns = [
    path('/', SupplierView.as_view()),
    path('/loc', SupplierLocationView.as_view()),
    ]