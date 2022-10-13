from django.urls import path  # django.urls의 path를 사용
from . import views  # 현재 app폴더 안에 views 사용

app_name = "articles"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
