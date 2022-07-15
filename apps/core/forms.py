from .models import Review, Order
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description', 'profile', 'product']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'profile': forms.HiddenInput(),
            'product': forms.HiddenInput(),
        }


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['surname', 'name', 'patronymic', 'address', 'postal_code', 'phone', 'email', 'comment']
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
