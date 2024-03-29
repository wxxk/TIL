from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import get_user_model

from django.contrib.auth import update_session_auth_hash
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('reviews:index')


def update(request):
    if request.method == "POST":
        pass
    else:
        form = CustomUserChangeForm(instance=request.user)
    context ={
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def detail(request, pk):
    user_detail = get_user_model().objects.get(pk=pk)
    context = {
        'user_detail':user_detail,
    }
    return render(request, 'accounts/detail.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("articles:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)

def delete(request, pk):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')