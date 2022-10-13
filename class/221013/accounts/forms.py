from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import User
from django.contrib.auth import get_user_model


class UsersForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ("username", "email")
