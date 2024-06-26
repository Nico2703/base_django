from django.shortcuts import render, redirect
from . import models, forms
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
    return render (request,"producto/index.html")

class ProductoList(ListView):
    model = models.Producto
    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list
    
class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoCategoriaForms
    success_url = reverse_lazy("producto:home")

    
class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoCategoriaForms
    success_url = reverse_lazy("producto:producto_list")

class ProductoDetail(DetailView):
    model = models.Producto

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")

