
from django import forms
from django.contrib.auth import get_user_model
from parsley.decorators import parsleyfy

@parsleyfy
class RegisterForm(forms.ModelForm):
    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'password',)


@parsleyfy
class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())