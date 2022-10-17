from django.shortcuts import redirect, render

from articles.models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/new.html", context)


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


def delete(reqeust, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")
