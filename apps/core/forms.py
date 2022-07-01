from .models import Product, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = User
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
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
