from django.urls import path
from .views import ProductAllView,ProductFavoriteView


urlpatterns = [
    path('/', ProductAllView.as_view()),
    path('/<int:pk>/favorite', ProductFavoriteView.as_view()),
    ]