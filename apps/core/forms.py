from .models import Review, Message
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('published', 'profile', 'product',)
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'profile': forms.HiddenInput(),
            'product': forms.HiddenInput(),
        }

    description = forms.CharField(label='Отзыв', min_length=10, widget=forms.Textarea(attrs={'class': 'form-control'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш e-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control'}))
