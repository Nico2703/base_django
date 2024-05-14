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
    return render (request,"cliente/index.html")

class ClienteList(ListView):
    model = models.Cliente

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Cliente.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Cliente.objects.all()
        return object_list
    
class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteCategoriaForms
    success_url = reverse_lazy("cliente:home")

    
class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteCategoriaForms
    success_url = reverse_lazy("cliente:cliente_list")

class ClienteDetail(DetailView):
    model = models.Cliente

class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")