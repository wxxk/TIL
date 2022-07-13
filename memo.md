# 헷갈리는 문법 정리

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

formoat(n, ".2f") # ".2f" 는 자리수 : 소수점 둘째자리까지 표시
formoat(n, ".3f") # 소수점 3째 자리까지 표시
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

