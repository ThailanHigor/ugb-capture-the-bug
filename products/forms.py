from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(), # algo está estranho aqui em!
        empty_label="Selecione",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows":3}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean_price(self):
        pass
