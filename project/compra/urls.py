from django.urls import path
from . import views

app_name = "compra"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("create/", views.CompraCreate.as_view(), name="compra_create"),
    path("list/", views.CompraList.as_view(), name="compra_list"),
    path("update/<int:pk>", views.CompraUpdate.as_view(), name="compra_update"),
    path("detail/<int:pk>", views.CompraDetail.as_view(), name="compra_detail"),
    path("delete/<int:pk>", views.CompraDelete.as_view(), name="compra_delete"),
]