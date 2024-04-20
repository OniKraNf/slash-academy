from typing import Any
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext as _
from .models import User

class SignUpForm(UserCreationForm):
    
    password1 = forms.CharField(
        label=('Password'),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control rounded-md', 'placeholder': 'Enter password'}),
    )
    
    password2 = forms.CharField(
        label=('Password'),
        strip=False,
        widget=PasswordInput(attrs={'class': 'form-control rounded-md', 'placeholder': 'Confirm password'}),
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control rounded-md', 'placeholder': 'Enter usename'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-md', 'placeholder': 'Enter email'}),
        }
        
    def clean_password1(self) -> str:
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 12:
            raise forms.ValidationError(_('Password must be at least 12 characters long.'))
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError(_('Password must contain at least one uppercase letter.'))
        return password1

    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control rounded-md', 'placeholder': 'Enter usename'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control rounded-md', 'placeholder': 'Enter password'}))