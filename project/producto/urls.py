from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "producto"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("list/", views.ProductoList.as_view(), name="producto_list"),
    path("update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
    path("detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"),
]

urlpatterns += staticfiles_urlpatterns()