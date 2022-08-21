from django.shortcuts import render
from allauth.account.views import LoginView, SignupView
from .forms import UserLoginForm, UserSignupForm


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = 'account/login.html'


class UserSignupView(SignupView):

    form_class = UserSignupForm
    template_name = 'account/signup.html'
