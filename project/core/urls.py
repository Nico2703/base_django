from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = "core"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("acerca/", views.acerca, name="acerca"),
]

urlpatterns += staticfiles_urlpatterns()