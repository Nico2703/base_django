from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}, {self.descripcion}"
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
