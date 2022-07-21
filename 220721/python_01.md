### 추가 문법

##### list comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  - `<expression> for <변수> in <interable>`
  - ````<expressgion for <변수> in <iterable> if <조건식>`
- 1~3의 세제곱의 결과가 담긴 리스트를 만드시오

```python 
cublic_list = []
for number in range(1, 4):
    cubic_list.appned(number**3)
print(cubic_list)

----------------------
[number**3 for number in range(1, 4)]
# => 특정한 원소(요소)로 구성원 리스트를 만들 때
```

##### dictionary comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
  - `{key: value for <변수> in <iterable>}`
  - `{key: vale for <변수> in <iterable> if <조건식>}`
- 1~3의 세제곱의 결과가 담긴 딕셔너리를 만드시오

```python
cubic_dict = {}
for number in range(1, 4)
	cubic_dict[number] = number ** 3
print(cubic_dict)

-----------------------------------------
{number: number ** 3 for number in range(1, 4)}
```

##### lambda [parameter] : 표현식

- 람다함수
  - 표현식을 계산한 결과값을 반환하는 함수로, **이름이 없는 함수여서 익명함수**라고도 불림
- 특징
  - **return문을 가질 수 없음**
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용 가능

##### filter

- `filter(function, iterable)`
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과가 True인 것들을 filter object로 반환

```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, number)
print(result, type(result))
-----------------------------
list(result) #리스트 형변환을 통해 결과 직접 확인
# [1, 3]
```

