from django.core.exceptions import ValidationError
from django import forms

from apps.core.models import Category, Product, Review, Order, Setting


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ('slug',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'published': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) > 5:
    #         raise ValidationError('Длина превышает 200 символов')
    #     return name


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug',)
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'volume': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'talk_forum': forms.TextInput(attrs={'class': 'form-control'}),
            'published': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('profile', 'product',)
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'published': forms.Select(attrs={'class': 'form-select'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('profile', 'products_price', 'delivery', 'total_price',)
        widgets = {
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'paid': forms.Select(attrs={'class': 'form-select'}),
            'profile': forms.Select(attrs={'class': 'form-select'}),
        }


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'
        exclude = ('name',)

        widgets = {
            'delivery': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_free': forms.TextInput(attrs={'class': 'form-control'}),
        }
