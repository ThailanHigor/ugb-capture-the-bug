from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control", "rows":3}))
    
    class Meta:
        model = Product
        fields = ["name", "description", "price", "active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
