from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows":3, "disabled": "disabled"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "disabled": "disabled"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
