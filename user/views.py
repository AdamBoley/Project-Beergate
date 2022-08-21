from allauth.account.views import LoginView, SignupView, PasswordChangeView, EmailView, PasswordSetView, PasswordResetView, PasswordResetFromKeyView
from .forms import UserLoginForm, UserSignupForm, UserChangePasswordForm, UserAddEmailForm, UserSetPasswordForm, UserResetPasswordForm, UserResetPasswordKeyForm


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = 'account/login.html'


class UserSignupView(SignupView):

    form_class = UserSignupForm
    template_name = 'account/signup.html'


class UserPasswordChangeView(PasswordChangeView):

    form_class = UserChangePasswordForm
    template_name = 'account/password_change.html'


class UserAddEmailView(EmailView):

    form_class = UserAddEmailForm
    template_name = 'account/email.html'


class UserPasswordSetView(PasswordSetView):

    form_class = UserSetPasswordForm()
    template_name = 'account/password_set.html'


class UserPasswordResetView(PasswordResetView):

    form_class = UserResetPasswordForm()
    template = 'account/password_reset.html'


class UserPasswordResetFromKeyView(PasswordResetFromKeyView):

    form_class = UserResetPasswordKeyForm()
    template_name = 'account/password_reset_from_key.html'
