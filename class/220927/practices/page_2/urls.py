from practices.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path("", views.home),
]
