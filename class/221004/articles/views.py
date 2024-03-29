from django.shortcuts import redirect, render

import articles
from .models import Article

# Create your views here.

# 요청 정보를 받아서
def index(request):
    # 게시글을 가져와서
    articles = Article.objects.order_by("-pk")
    # template에 전달한다.
    context = {"articles": articles}

    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/new.html")


def create(request):
    # DB에 저장하는 로직
    title = request.POST.get("title")
    content = request.POST.get("content")

    Article.objects.create(title=title, content=content)

    return redirect("articles:index")


def edit(request, pk):
    articles = Article.objects.get(pk=pk)
    context = {"articles": articles}
    return render(request, "articles/edit.html", context)


def update(request, pk):
    articles = Article.objects.get(pk=pk)
    # print("hi")
    articles.title = request.POST.get("title")
    articles.content = request.POST.get("content")
    articles.save()

    return redirect("articles:index")
