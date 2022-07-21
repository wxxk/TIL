### 객체지향 프로그래밍

> 객체 지향 프로그래밍은 컴퓨터 프로그래밍의 패러다임 중 하나이다. 
>
> 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 
>
> 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메세지를 주고받고, 데이터를 처리할 수 있다.

**파이썬은 모든 것이 객체(object) => 대상의 정보와 동작 (S + V)**



##### 객체(object)는 특정 타입의 인스턴스(instance)이다.

> 123, 900, 5는 모두 int의 인스턴스
>
> 'hello', 'bye'는 모두 string의 인스턴스
>
> [232, 89,1] []은 모두 list의 인스턴스



##### 객체의 특징

- 타입 : 어떤 연산자와 조작이 가능한가
- 속성 : 어떤 상태를 가지는가
- 조작법 : 어떤 행위를 할 수 있는가



##### 객체지향 프로그래밍이란

- 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법
- 절차지향 프로그래밍 vs 객체지향 프로그래밍

```python
# 절차지향 프로그래밍
def area(x, y):
    return x * y
def circumference(x, y):
    return 2 * (x + y)
a = 10
b = 30
c = 300
d = 20
suqare1_area = area(a, b)
square1_circumference = circumference(a, b)
suqrae2_area = area(a, b)
square2_circumference = cirecumference(a, b)
```

```python
# 객체지향 프로그래밍
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    def circumference(self):
        return 2 * (self.x + self.y)
r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

> 사각형 - 클래스(class)
>
> 각 사각형(R1, R2) - 인스턴스(instance)
>
> 사각형의 정보 - 속성(attribute) : 가로/세로 길이
>
> 사각형의 행동 기능 - 메소드(method) : 넓이를 구한다. 높이를 구한다.



##### 객체지향의 장점

- 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 대문에 대규모 소프트웨어 개발에 많이 사용
- 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 직관적인 코드 분석을 가능하게 한다

