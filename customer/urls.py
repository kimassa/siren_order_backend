from django.urls import path
from .views import CustomerSignUpView, CustomerSignInView


urlpatterns = [
    path('/', CustomerSignUpView.as_view()),
    path('/signin', CustomerSignInView.as_view()),
    ]