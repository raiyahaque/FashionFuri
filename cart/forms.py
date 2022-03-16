from django import forms
CLOTHING_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,10)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices = CLOTHING_QUANTITY_CHOICES,
        coerce=int, label='')

    new_quantity = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
