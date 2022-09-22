from re import I
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 환영하는 메인 페이지를 보여준다.
    names =['이상욱', '지현식', '김윤지', '김예린', '문경욱', '김유영', '류진숙', '박찬솔', '문상희', '이유주', '하승찬']
    name = random.choice(names)
    context ={
        # 변수명 : 값
        'name' : name,
        'img' : 'https://i.pinimg.com/564x/b7/18/b7/b718b792b6266d4b8ab25dfc630908d3.jpg'
    }
    return render(request, 'index.html', context)


def welcome(request, name):
    # 사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이르을 동시에 보여준다.
    context = {
        'name': name,
        'greetings':[
            '안녕하세요', 'hello', 'guten tag', 'bon jour'
        ],
        'images': [
            'https://i.pinimg.com/564x/71/24/62/7124628d655696e18639c1367704ba02.jpg',
            'https://i.pinimg.com/564x/71/f0/46/71f04685e5c9df3d491517494d17697b.jpg',
            'https://i.pinimg.com/564x/72/16/43/7216431742ba20b6b5e733a59b6d42f8.jpg',
        ],
    }
    return render(request, 'welcome.html', context)
