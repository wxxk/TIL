from django.urls import URLPattern, path
from . import views

app_name = "reviews"

urlpatterns = [
    path("reviews/", views.index, name="index"),
    path("reviews/create/", views.create, name="create"),
    path("reviews/<int:pk>/", views.detail, name="detail"),
    path("reviews/<int:pk>/update/", views.update, name="update"),
    path("reviews/<int:pk>/delete/", views.delete, name="delete"),
    path("reviews/search/", views.search, name="search"),
    path("<int:pk>/comments/", views.comments_create, name="comments_create"),
    path("<int:review_pk>/comments/<int:comment_pk>/delete/", views.comments_delete, name='comments_delete'),
]
