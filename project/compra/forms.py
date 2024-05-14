from django import forms
from . import models

class CompraCategoriaForms(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = "__all__"
        widgets = {
            "precio": forms.TextInput(attrs={"class":"form-comtrol}"}),
        }