from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, "page_1/index.html")


def home(request):
    return render(request, "page_1/home.html")
