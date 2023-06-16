from django.contrib.auth.forms import AuthenticationForm , UserCreationForm


class MyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'password'
        })


class MyRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password1',
            'placeholder': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password2',
            'placeholder': 'password'
        })