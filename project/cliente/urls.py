from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "cliente"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("create/", views.ClienteCreate.as_view(), name="cliente_create"),
    path("list/", views.ClienteList.as_view(), name="cliente_list"),
    path("update/<int:pk>", views.ClienteUpdate.as_view(), name="cliente_update"),
    path("detail/<int:pk>", views.ClienteDetail.as_view(), name="cliente_detail"),
    path("delete/<int:pk>", views.ClienteDelete.as_view(), name="cliente_delete"),
]

urlpatterns += staticfiles_urlpatterns()

