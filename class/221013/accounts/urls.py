from django.urls import path  # django.urls의 path를 사용
from . import views  # 현재 app폴더 안에 views 사용

# 로그인

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("password/", views.change_password, name="change_password"),
]
