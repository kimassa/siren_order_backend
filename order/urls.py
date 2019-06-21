from django.urls import path
from .views import OrderView, OrderReadyView


urlpatterns = [
    path('/', OrderView.as_view()),
    path('/orders/', OrderReadyView.as_view()),
    ]