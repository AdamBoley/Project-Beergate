from django.urls import path
from allauth.account.views import LogoutView
from .views import UserLoginView, UserSignupView, UserPasswordChangeView

urlpatterns = [
    path(
        'account/signin/',
        UserLoginView.as_view(),
        name='account_login'
        ),
    path(
        'account/signout/',
        LogoutView.as_view(),
        name='account_logout'
        ),
    path(
        'account/signup/',
        UserSignupView.as_view(),
        name='account_signup'
        ),
    path(
        'account/password/change/',
        UserPasswordChangeView.as_view(),
        name='account_change_password'
        ),
]
