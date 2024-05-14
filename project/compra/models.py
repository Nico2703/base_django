from django.db import models
from producto.models import Producto
from cliente.models import Cliente
from django.contrib.auth.models import User
from django.utils import timezone

class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="vendedor")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return self.usuario.username
    
    class Meta:
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"
    
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "cliente")
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= "producto")
    precio = models.CharField(max_length=20)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name= "vendedor")
    fecha = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.cliente}, {self.producto}, {self.precio}, {self.vendedor}, {self.fecha}"
    
    class Meta:
        verbose_name = "compra"
        verbose_name_plural = "compras"


