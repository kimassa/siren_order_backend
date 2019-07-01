from django.urls import path
from .views import UserSignUpView, UserSignInView, UserFrequencyView


urlpatterns = [
    path('/', UserSignUpView.as_view()),
    path('/signin', UserSignInView.as_view()),
    path('/frequency/<int:pk>', UserFrequencyView.as_view()),
    path('/frequency/<int:pk>/update', UserFrequencyView.as_view()),
    ]