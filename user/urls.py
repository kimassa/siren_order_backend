from django.urls import path, include
from .views import UserFrequencyView, ProfileViewSet

from user import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', ProfileViewSet, basename="users")


urlpatterns = [
    path('/frequency/<int:pk>', UserFrequencyView.as_view()),
    path('/frequency/<int:pk>/update', UserFrequencyView.as_view()),
    path('/profile/', include(router.urls)),
]