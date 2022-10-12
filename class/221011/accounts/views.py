from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "accounts/home.html", context)


def signup(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()

            # 로그인
            # cleaned = 검증된 후에 데이터가 들어가는 변수
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username, password=raw_password)
            login(request, user)

            return redirect("accounts:home")
    else:
        form = UsersForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user1": user}
    return render(request, "accounts/detail.html", context)
