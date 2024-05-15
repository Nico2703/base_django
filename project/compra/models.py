from django.db import models
from producto.models import Producto
from cliente.models import Cliente
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ValidationError


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
    precio_total = models.FloatField(editable=False, blank=True, null=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name= "vendedor")
    cantidad = models.PositiveIntegerField(null=True)
    fecha = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.cliente}, {self.producto}, {self.cantidad}, {self.precio_total}, {self.vendedor}, {self.fecha}"
    
    class Meta:
        verbose_name = "compra"
        verbose_name_plural = "compras"

    def clean(self):
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("La cantidad vendida no puede ser mayor a la cantidad disponible")

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)
