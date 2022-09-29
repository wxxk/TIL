import re
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by("deadline", "priority")
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


def edit(request, pk):
    todos = Todo.objects.get(pk=pk)
    context = {
        "todos": todos,
    }
    return render(request, "todos/edit.html", context)


def update(request, pk):
    # update할 특정 데이터를 불러온다 ->pk를 사용해서
    todos = Todo.objects.get(pk=pk)

    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    # 데이터를 수정
    todos.content = content
    todos.priority = priority
    todos.deadline = deadline

    # 저장
    todos.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect("todos:detail", todos.pk)


def detail(request, pk):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다.
    # 불러온 데이터를 todos에 할당
    todo = Todo.objects.get(pk=pk)

    context = {
        "todo": todo,
    }

    return render(request, "todos/detail.html", context)


def delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect("todos:index")


def change(request, pk):
    todo = Todo.objects.get(id=pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True

    todo.save()

    return redirect("todos:index")
