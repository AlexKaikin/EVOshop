from .models import Product, Review, Order
from django import forms


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


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['surname', 'name', 'patronymic', 'address', 'postal_code', 'phone', 'email', 'comment']
