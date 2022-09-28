from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos_ = Todo.objects.all()
    context = {
        "todos": todos_,
    }

    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content_")

    Todo.objects.create(content=content)

    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect("todos:index")
