from . import views
from django.urls import path
from allauth.account.views import LoginView, SignupView
from .views import UserLoginView, UserSignupView

urlpatterns = [
    path('account/login/', UserLoginView.as_view(), name='account_login'),
    path('account/signup/', UserSignupView.as_view(), name='account_signup')
]
