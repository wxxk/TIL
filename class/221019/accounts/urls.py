from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
    path('password/', views.change_password, name='change_password'),
    path("<int:pk>/delete/", views.delete, name="delete"),
]