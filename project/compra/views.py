from django.shortcuts import render, redirect
from . import models, forms
from .models import Compra, Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

def home(request):
    return render (request,"compra/index.html")

class CompraList(ListView):
    model = models.Compra

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Compra.objects.filter(cliente__apellido__icontains=consulta)
        else:
            object_list = models.Compra.objects.all()
        return object_list
    
class CompraCreate(CreateView):
    model = models.Compra
    form_class = forms.CompraCategoriaForms
    success_url = reverse_lazy("compra:home")

class CompraUpdate(UpdateView):
    model = models.Compra
    form_class = forms.CompraCategoriaForms
    success_url = reverse_lazy("compra:compra_list")

class CompraDetail(DetailView):
    model = models.Compra

class CompraDelete(LoginRequiredMixin, DeleteView):
    model = models.Compra
    success_url = reverse_lazy("compra:compra_list")
    
