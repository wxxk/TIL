from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }
    return redirect("todos:index")


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todos:index")
