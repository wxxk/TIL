# 헷갈리는 문법 정리

#### 깃 리모트 변경 하기

- 기존 리포지토리 깔끔하게 pull / push

```
git pull
git add .
git commit -m "clean push"
git push
테스트
```

- 기존 리포지토리 remote 제거

```
git remote remove origin
```

- 새 리포지토리 remote 추가

```
git remote add origin https://github.com/계정/리포지토리
```



---

#### fork



---

#### pull



---

#### split

```python
a, b = input().split()
```

- input()은 한 줄 단위로 입력을 받는다.
- input().split() 를 사용하면, 공백기준으로 입력된 값들을 나누어 자른다.
  - split('문자') : `('문자')` 를 기준으로 입력된 값들을 나누어 자른다 



---

#### sep

```python
print(?, ?, sep=:':') # `:`기호를 사이에 두고 값을 출력한다.
```



---

### f-sting

```python
print(2020년 1월)
print(2020년 2월)
...
print(2020년 12월)
```

```python
month = 1
while month <= 12
	print(f'2020년 {month}월')
    month = month + 1
```

- `print(f'')`: `''`사이에 내용 입력, 변수는 `{}`로 묶어줌



---

#### range

```python
# 0부터 9까지의 범위를 만들고 싶다면
num in range(10)
```

- `<종류값> - 1`까지 범위 생성
- 기본문법
  - `range(<시작값>, <종료값>, <증분>)`
  - `range(<시작값>, <종료값>)` : 범위 내의 숫자 1씩 증가
  - range(<종료값>) : 1개는 종료값으로 사용, 시작값은 `0`으로 적용

- 응용

``` python
letters = ['A', 'B', 'C', 'D', 'E', 'F'] 
#list
#  0   1   2   3   4
# -5  -4  -3  -2  -1
# "A" "B" "C" "D" "E"

for idx in range(len(letters)):
    print(letters[idx])
```



---

### 진수

```python 
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
n = int(a, 8)      #입력된 a를 16진수로 인식해 변수 n에 저장
```



---

### format

- format(숫자, ".2f") : 원하는 자리까지의 정확도로 반올림 된 실수 값을 만듬
- `".2f"`는 자리수를 의미(소수점 둘째 자리까지 표시)
  - `".3f"`: 소수점 3째자리까지 표시

```python
n = float(input())

format(n, ".2f") # ".2f" 는 자리수 : 소수점 둘째자리까지 표시
format(n, ".3f") # 소수점 3째 자리까지 표시
```



---

### 코드

- 아스키코드 : 128개의 문자조합을 제공하는 7비트 부호
- 유니코드 : 각 나라별 언어를 모두 표현하기 위해 나온 코드 체계
  - 숫자와 글자, 즉 키값이 1:1로 매핑된 형태의 코드
- UTF-8 : 유니코드를 사용하는 인코딩 방식 중하나
  - 영문/숫자/기호는 1바이트로, 한글/한자는 3바이트로 표현
  - 전세계 모든 글자들을 한꺼번에 표현할 수 있다.



- ord() : 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수

```python
a = ard('A') 
# b = ord('EE') -> error 한 글자만 가능
# c = ord(123) -> error number X
d = ord('ㅁ')
e = ord('B')
f = hex(ord('B')) # 16진수

print(a)
print(d)
print(e)
print(f)

#결과
65
12609
66
0x42
```

- chr() : 아스키 코드 값을 문자로 변환하여 반환(10진수, 16진수 사용 가능)

```python
a = chr(123)
# b = chr(-123) -> error 0x110000 사이의 수만가능
# c = chr('d') -> error 문자열 불가
d = chr(66) # 'B'의 아스키코드
e = chr(0x42) # 'B'의 아스키코드 16진수 값

print(a)
print(d)
print(e)

#결과
<
B
B
```



---

### 진수

```python
a,b = map(int, input().split())

print('%o'% a) # 8진수로 출력
print('%x'% b) # 16진수로 출력(소문자)
print('%X'% b) # 16진수로 출력(대문자)


c = input()
n = int(c, 16) # 16진수로 입력받기
```



---

### map

- 반복 가능한 객체(것)들의 모든 요소에 각각 특정 함수를 적용한 결과들로 구성된 것으로 나타내려고 하는 것

```python
a, b = map(int, input().split())
# input().split()의 결과인 리스트의 모든 요소에 각각 int 형변환 함수를 적용한 결과로 구성된 것
```



---

### <<

왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
가장 오른쪽에 있는 1비트는 사라진다.

예시
n = 10
print(n<<1) #10을 2배 한 값인 20 이 출력된다.
print(n>>1) #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2) #10을 4배 한 값인 40 이 출력된다.
print(n>>2) #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.



---

### bool

a = bool(int(input()))

참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서 not 예약어(reserved word, keyword)를 사용할 수 있다.

이러한 논리연산을 NOT 연산(boolean NOT)이라고도 부르고,
프라임 '(문자 오른쪽 위에 작은 따옴표), 바(기호 위에 가로 막대), 문자 오른쪽 위에 c(여집합, complement) 등으로 표시한다.
모두 같은 의미이다.

참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있고,
불 값들 사이의 논리(not, and, or) 연산 결과도 마찬가지로 True 또는 False 의 불 값으로 계산 된다.

정수값 0은 False 이고, 나머지 정수 값들은 True 로 평가된다.
빈 문자열 "" 나 ''는 False 이고, 나머지 문자열들은 True 로 평가된다.

** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로 True(참)/False(거짓) 값만 가지는 논리값과 그 값들 사이의 연산을 다룬다.



---



### F 스트링



---



### 3항 연산

가장 큰 값 : (a if a>b else b) if ((a if a>b else b)>c) else c

가장 작은 값 : (a if a<b else b) if ((a if a<b else b)<c) else c



---



### 파이썬의 Asterisk(*) 이해하기

1. 곱셈 및 거듭제곱 연산으로 사용할 때

```python
>>> 2 * 3
6
>>> 2 ** 3
8
>>> 1.414 * 1.414
1.9999999999999997
>>> 1.414 ** 1.414
1.6320575353248798
```

2. 리스트형 컨테이너 타입의 데이터 반복을 확장하고자 할 때

```python
# 길이 100의 제로값 리스트 초기화
zeros_list = [0] * 100

# 길이 100의 제로값 튜플 선언
zeros_tuple = (0,) * 100
```

3. 가변인자를 사용하고자 할 때

> 들어오는 인자의 갯수를 모를 때
>
> 그 어떤 인자라도 모두 받아서 처리 해야할 때

- positional arguments : 위치에 따라 정해지는 인자(생략 불가능 / 정해진 갯수대로 정해진 위치에 인자를 전달)
- keyword arguments : 키워드(이름)을 가진 인자(함수 선언시 디폴트값 설정 가능 / 생략시 디폴트 값이 들어감)

```python 
# 2~4명의 주자로 이루어진 달리기 대회 랭킹을 보여주는 함수
def save_ranking(first, second, third=None, fourth=None):
    # first, second = positional arguments
    # third, fourth = keyword arguments
    rank = {}
    rank[1], rank[2] = first, second 
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)
    
    # positional arguments 2개 전달
	save_ranking('ming', 'alice')
	# positional arguments 2개와 keyword argument 1개 전달
	save_ranking('alice', 'ming', third='mike')
	# positional arguments 2개와 keyword arguments 2개 전달 (단, 하나는 positional argument 형태로 전달)
	save_ranking('alice', 'ming', 'mike', fourth='jim')
```

4. 컨테이너 타입의 데이터를 Unpacking 할 때

> list나 tup;e 또는 dict 형태의 데이터를 가짐
>
> 어떤 함수가 가변인자를 받는 경우 사용 가능

```python
from functools import reduce

primes = [2, 3, 5, 7, 11, 13]

def product(*numbers):
    p = reduce(lambda x, y: x * y, numbers)
    return p

product(*primes)
# 30030

product(primes)
# [2, 3, 5, 7, 11, 13]
```

