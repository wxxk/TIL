from django.contrib import admin
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.signup, name="signup"),
    path("home/", views.home, name="home"),
    path("<int:pk>/", views.detail, name="detail"),
    path("login/", views.login, name="login"),
]
