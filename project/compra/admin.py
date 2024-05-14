from django.contrib import admin
from . import models


class CompraAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "producto",
        "precio",
        "fecha",
    )
    list_display_links = ("producto",)
    search_fields = ("producto.nombre", "vendedor")
    list_filter = ("vendedor",)
    date_hierarchy = "fecha"

admin.site.register(models.Compra)
admin.site.register(models.Vendedor)