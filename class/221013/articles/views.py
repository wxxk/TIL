from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from articles.models import Article
from .forms import ArticleForm

from django.contrib import messages

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "글 작성이 완료 되었습니다.")
        return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()

            return redirect("articles:detail", article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
        "article": article,
    }
    return render(request, "articles/update.html", context)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")
