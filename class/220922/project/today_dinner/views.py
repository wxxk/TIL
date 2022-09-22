from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    menus = [
        ['족발', 'https://i.pinimg.com/564x/fe/8f/a3/fe8fa36d801f1e24ef34df9ee32bb11c.jpg'],
        ['돈까스', 'https://i.pinimg.com/564x/ea/52/04/ea52043da8f6fa09764bce5b46d67b47.jpg'],
        ['삼겹살', 'https://i.pinimg.com/564x/a9/f8/1e/a9f81eae28b6e46a70908ffea298e882.jpg'],
        ['피자','https://i.pinimg.com/736x/07/38/54/0738544d84fb1399d955555ba4ed37af.jpg'],
        ['중식', 'https://i.pinimg.com/564x/8c/64/e9/8c64e9115e26b58c709cc85a4795345c.jpg'],
        ['치킨', 'https://i.pinimg.com/736x/49/70/31/4970315bc64284052adc2dd17cfa1d03.jpg'],
        ['버거', 'https://i.pinimg.com/736x/c6/52/19/c6521996cd56c63a342929a9e27d7aa4.jpg'],
        ['분식', 'https://i.pinimg.com/564x/cd/89/77/cd89772271dfdb3a1afa6321a745bf40.jpg']
    ]
    menu = random.choice(menus)
    context = {
        'menu' : menu[0],
        'image' : menu[1],
    }
    return render(request, 'today_dinner.html', context)

def lotto(request):
    lotto_list = []

    for i in range(5):
        lotto = random.sample(range(1, 45), 6)
        lotto.sort()

        lotto_list.append(lotto)

        context = {
            'lotto' : lotto_list
        }

    return render(request, 'lotto.html', context)