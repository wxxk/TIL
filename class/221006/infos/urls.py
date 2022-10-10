from django.urls import path
from . import views

app_name="infos"

urlpatterns=[
    path('movies/', views.movies, name='movies'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('search/', views.search, name='search'),   
]
