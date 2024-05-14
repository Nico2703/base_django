from django import forms
from . import models

class ProductoCategoriaForms(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class":"form-comtrol}"}),
            "descripcion": forms.TextInput(attrs={"class":"form-comtrol}"}),
        }