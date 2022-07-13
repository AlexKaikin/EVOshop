from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from apps.core.models import Profile


class UserRegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class UserLoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
