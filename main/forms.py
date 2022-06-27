from django.forms import ModelForm
from .models import Review
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
