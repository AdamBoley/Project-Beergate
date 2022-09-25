from allauth.account.views import LoginView, SignupView, PasswordChangeView, EmailView, PasswordSetView, PasswordResetView, PasswordResetFromKeyView
from .forms import UserLoginForm, UserSignupForm, UserChangePasswordForm, UserAddEmailForm, UserSetPasswordForm, UserResetPasswordForm, UserResetPasswordKeyForm


class UserLoginView(LoginView):
    """
    Custom login view that extends that AllAuth LoginView
    sets form_class to custom UserLoginForm
    """

    form_class = UserLoginForm
    template_name = 'account/login.html'


class UserSignupView(SignupView):
    """
    Custom Signup/register view that extends AllAuth SignupView
    sets form_class to custom UserSignupForm
    """

    form_class = UserSignupForm
    template_name = 'account/signup.html'


class UserPasswordChangeView(PasswordChangeView):
    """
    Custom view for changing user account password
    Extends AllAuth PasswordChangeView
    sets form_class to custom UserChangePasswordForm
    success_url specifies redirection to landing page
    """

    form_class = UserChangePasswordForm
    template_name = 'account/password_change.html'
    success_url = '/'


class UserAddEmailView(EmailView):
    """
    Custom view for adding an email address to a user account
    Extends AllAuth EmailView
    sets form_class to custom UserAddEmailForm
    IMPORTANT - currently inactive due to requiring an email server
    Retained for future work
    """

    form_class = UserAddEmailForm
    template_name = 'account/email.html'


class UserPasswordSetView(PasswordSetView):
    """
    Custom view for adding a password to a user account
    Used if an account has been created through AllAuth Social Account functionality
    Extends AllAuth PasswordSetView
    sets form_class to custom UserPasswordSetForm
    IMPORTANT - currently inactive due to requiring an email server
    Retained for future work
    """

    form_class = UserSetPasswordForm()
    template_name = 'account/password_set.html'


class UserPasswordResetView(PasswordResetView):
    """
    Custom view for resetting the password of a user account
    Extends AllAuth PasswordResetView
    sets form_class to custom UserPasswordResetForm
    IMPORTANT - currently inactive due to requiring an email server
    Retained for future work
    """

    form_class = UserResetPasswordForm()
    template = 'account/password_reset.html'


class UserPasswordResetFromKeyView(PasswordResetFromKeyView):
    """
    Custom view for resetting the password of a user account from an emailed key
    Extends AllAuth PasswordResetFromKeyView
    sets form_class to custom UserPasswordResetFromKeyView
    IMPORTANT - currently inactive due to requiring an email server
    Retained for future work
    """

    form_class = UserResetPasswordKeyForm()
    template_name = 'account/password_reset_from_key.html'
