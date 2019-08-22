from django.urls import path
from .views import UserFrequencyView

from user import views

urlpatterns = [
    path('/frequency/<int:pk>', UserFrequencyView.as_view()),
    path('/frequency/<int:pk>/update', UserFrequencyView.as_view()),

]