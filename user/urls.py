from . import views
from django.urls import path
# from allauth.account.views import LoginView, SignupView
from .views import UserLoginView, UserSignupView, UserPasswordChangeView, UserAddEmailView, UserPasswordSetView, UserPasswordResetView, UserPasswordResetFromKeyView

urlpatterns = [
    path('account/login/', UserLoginView.as_view(), name='account_login'),
    path('account/signup/', UserSignupView.as_view(), name='account_signup'),
    path('account/password/change/', UserPasswordChangeView.as_view(), name='account_change_password'),
    path('account/password/reset/', UserPasswordResetView.as_view(), name='account_reset_password'),
    path('account/password/set/', UserPasswordSetView.as_view(), name='account_set_password'),
    path('account/email/', UserAddEmailView.as_view(), name='account_email'),
]
