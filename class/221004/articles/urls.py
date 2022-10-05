# URL 설정을 app 단위로 진행!

from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("update/<int:pk>/", views.update, name="update"),
]
