from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class  Meta:
        model = Product
        fields = ['title', 'status']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget_attrs.update({
            'class': 'form-control'
        })