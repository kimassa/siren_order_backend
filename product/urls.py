from django.urls import path
from .views import AllProductView


urlpatterns = [
    path('/', AllProductView.as_view()),
    ]