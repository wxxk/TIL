# 객체지향 프로그래밍2

### 목차

- [객체지향 프로그래밍](README.md)

- [클래스](object_2_01.md)

- [객체 지향의 핵심개념](object_2_02.md)

  

---

객체는 **속성**과 **메서드**(기능을 담당)가 존재하는 모습이다.

 이 모습을 클래스로 정의하고, 실질적으로 사용하는 것은 개별 인스턴스이다.

함수는 input이 들어오면 output을 리턴한다.

```
class Person:
    pass

p1 = Person() # 인스턴스 생성 
p1.name = '홍길동' # 인스턴스 속성

print(p1.name) 
#출력 홍길동
class Person:

    def greeting(self): # 인스턴스 메서드 (인스턴스가 활용할 메서드이다.)
        print('안녕하세요~!')

iu = Person() # ()는 메서드를 호출한다. 
iu.greeting() # 인스턴스가 메서드를 실행시키고 있다.  
class Person:
    species = '사람' #클래스 변수

print(Person.species) # 클래스 변수(속성)
```



### self

인스턴스를 만들 때는 이름 정보를 받아서 하고자 한다.

```
class Person:
    def __init__(self, name): # 인풋 2개를 받아서 함수 내에서 쓰겠다는 선언

        # 개별 인스턴스에 각각 name 속성을 지정하고자 한다. 
        self.name = name

# 인스턴스 만들 때
jimin = Person('지민')
print(jimin.name) 

#출력 지민
```

Q. **Input 2개(self, name)를 넣어 활용하기로 했으면서,**

**jimin = Person('지민')에서 1개 ('지민')만 넣는 이유는?**

A. 내부적으로 모든 인스턴스 메서드 중 (def init (self, name):) 첫 번째로 self를 넘겨준다는 약속이 되어있다.

즉, 내부적으로 호출될 때에는 다른 모습이 숨겨져 있다.



```
def greeting(self):
    print('안녕하세요, 지민입니다.')

jimin = Person('지민')
jimin.greeting()

iu = Person('지은')
iu.greeting()
# 출력 안녕하세요, 지민입니다.
# 안녕하세요, 지민입니다.
def greeting(self):
    print('안녕하세요, {self.name}입니다.')

jimin = Person('지민')
jimin.greeting()

iu = Person('지은')
iu.greeting()
# 출력 안녕하세요, 지민입니다.
# 안녕하세요, 지은입니다.
```

jmin.greeting()은 내부적으로 Person.greeting(jimin) 이런 느낌으로 항상 넘겨준다.

self의 의미는 호출하는 인스턴스를 파이썬 내부적으로 전달해준다.

즉, jimin = Person('지민')에서 1개의 값 ('지민')만 넣어줘도 내부적으로 self의 값도 들어가기 때문에 2개의 인풋이 들어오는 것으로 인식하는 것이다.



랜덤한 로또 번호를 출력하는 코드를 작성해보자.

```
import random

for i in range (5)
    numbers = range(1, 46)
    result = random.sample(numbers, 6)
    result.sort()
    print(result)
```

이 코드를 바탕으로 클래스와 함수를 만들었다고 가정해보자.

```
# 함수.ver
import lotto_function

buy_numbers = lotto_function.generate_lotto(5)
lotto_function.check(buy_number, [1, 2, 3, 4, 5, 6])
```

input을 넣으면 output을 주는 것 뿐이다. 이외의 행위를 할 수 없다.

```
# 클래스.ver

import lotto_clss

lotto = lotto_class.Lotto() # lotto는 인스턴스
lotto.generate_lotto() # 생성해 (verb)
print(lotto.numbers)    # 숫자 출력해
print(lotto.get_money([1, 2, 3, 4, 5, 6])) # 당첨 확인해
```

lotto 인스턴스로 속성(numbers)을 볼 수 있고, 생성하고 확인(get_money)할 수 있다. (다양한 행위가 가능하다)

**다시 말해, 클래스를 정의한다는 것은 하나의 타입이 속성(데이터)을 가지고 있고, 어떠한 메서드(행위)를 할 수 있다는 것이다. **

**이 점에서 함수와는 다르게 클래스는 객체를 조작할 수 있는 형태를 가지고 있다. **