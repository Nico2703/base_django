from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.nacimiento}"

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
