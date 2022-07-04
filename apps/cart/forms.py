from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    quantity = forms.IntegerField(max_value=10, min_value=1, initial=1, label='')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
