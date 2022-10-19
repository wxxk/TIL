from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from articles.models import Article
from .forms import ArticleForm, CommentForm

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
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
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
    comment_form = CommentForm()
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
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

    else:
        from django.http import HttpResponseForbidden

        return HttpResponseForbidden()


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.pk == article.pk:
        article.delete()
        return redirect("articles:index")
    else:
        from django.http import HttpResponseForbidden

        return HttpResponseForbidden()


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect("articles:detail", article.pk)
