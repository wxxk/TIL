from django.shortcuts import render

# Create your views here.
from day3pjt.settings import BASE_DIR
from .models import Article

guestbook = []


def index(request):
    # DB에서 가져오기
    guestbook = Article.objects.all()
    # SELECT * FROM articles;

    return render(request, "articles/index.html", {"guestbook": guestbook})


def create(request):
    content = request.GET.get("content")
    # guestbook.append(content)
    # DB에 저장
    Article.objects.create(content=content)

    return render(request, "articles/create.html", {"content": content})
