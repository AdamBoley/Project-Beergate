from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm, AddEmailForm, SetPasswordForm, ResetPasswordForm, ResetPasswordKeyForm


class UserLoginForm(LoginForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    """

    def __init__(self, *args, **kwargs):
        """
        Applies Bootstrap form-control class to login and password fields
        """
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })


class UserSignupForm(SignupForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    """

    def __init__(self, *args, **kwargs):
        """
        Applies Bootstrap form-control class to all fields using a for loop
        """
        super(UserSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class UserChangePasswordForm(ChangePasswordForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    """

    def __init__(self, *args, **kwargs):
        """
        Applies Bootstrap form-control class to all fields using a for loop 
        """
        super(UserChangePasswordForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class UserAddEmailForm(AddEmailForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    IMPORTANT - currently not in use
    Corresponding UserAddEmailView is not active
    """

    def __init__(self, *args, **kwargs):
        """
        Applies Bootstrap form-control class to all fields using a for loop
        """
        super(UserAddEmailForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class UserSetPasswordForm(SetPasswordForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    IMPORTANT - currently not in use
    Corresponding UserSetPasswordView is not active
    """

    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class UserResetPasswordForm(ResetPasswordForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    IMPORTANT - currently not in use
    Corresponding UserResetPasswordView is not active
    """

    def __init__(self, *args, **kwargs):
        """
        Applies Bootstrap form-control class to all fields using a for loop
        """
        super(UserResetPasswordForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class UserResetPasswordKeyForm(ResetPasswordKeyForm):
    """
    Custom UserLoginForm
    Extends AllAuth LoginForm
    Primarily written to apply Bootstrap classes
    All functionality contained within __init__ method
    IMPORTANT - currently not in use
    Corresponding UserResetPasswordFromKeyView is not active
    """

    def __init__(self, *args, **kwargs):
        """
        Applies Bootstrap form-control class to all fields using a for loop
        """
        super(UserResetPasswordKeyForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })
