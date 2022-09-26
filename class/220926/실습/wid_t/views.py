from django.shortcuts import render
import random

# Create your views here.
def isoddeven(request, num):

    number = num

    if number == 0:
        check = 0
    else:
        if number % 2:
            check = "홀수"
        else:
            check = "짝수"
    context = {
        "num": number,
        "check": check,
    }

    return render(request, "isoddeven.html", context)


def number(request):
    return render(request, "number.html")


def calculate(request, number1, number2):
    num1 = number1
    num2 = number2

    context = {
        "num1": num1,
        "num2": num2,
        "a": num1 + num2,
        "b": num1 - num2,
        "c": num1 * num2,
        "d": num1 // num2,
    }

    return render(request, "calculate.html", context)


def name(request):
    return render(request, "name.html")


def random_(request):
    name = request.GET.get("name")
    past_life = [
        "너구리",
        "강아지",
        "쥐",
        "하이에나",
        "거북이",
        "고릴라",
        "토끼",
        "고슴도치",
        "돼지",
        "늑대",
        "여우",
        "양",
        "족제비",
        "고양이",
        "새",
        "잼민이",
    ]

    past = random.choice(past_life)

    context = {"name": name, "past": past}
    return render(request, "random_.html", context)
