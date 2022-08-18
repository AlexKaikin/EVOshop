from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
import re

from .models import Profile


class UserRegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    username = forms.CharField(label='Логин пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.TextInput(attrs={'class': 'form-control'}))
    checkbox = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        regex = '^[a-z0-9]+$'
        compilation = re.compile(regex)  # compiling regex
        comparison = re.search(compilation, username)  # searching regex
        if comparison:  # validating conditions
            return cleaned_data
        else:
            self.add_error('username',
                           'Разрешаются только буквы латинского алфавита в нижнем регистре и цифры, без пробелов!')


class UserLoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'password']

    username = forms.CharField(label='Логин пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'username', 'email', 'first_name', 'last_name']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
        }

    username = forms.CharField(label='Логин пользователя',
                               widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}))
    email = forms.EmailField(label='Адрес электронной почты',
                             widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}))
