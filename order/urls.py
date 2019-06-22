from django.urls import path
from .views import OrderView, OrderStatusView


urlpatterns = [
    path('/', OrderView.as_view()),
    path('/orders/', OrderStatusView.as_view()),
    path('/status/', OrderStatusView.as_view()),
    ]