from allauth.account.forms import LoginForm, SignupForm
from django.utils.translation import gettext_lazy as _
from django import forms


class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })


class UserSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })
