# 입력 & 출력



### 입력 활용 예시

##### input()

- input()은 사용자의 입력 한 줄을 문자열로 받는 함수

```python
word = input()
>>> happyhacking
```

- map()

```python
# 문자열로 입력
a = input()

# 한 개 숫자로 입력
b = int(input())
c = float(inout())

# 여러 개 숫자로 입력
d, e = map(int, input().split())
f, g, h = map(float, input().split())
```



### 출력 활용 예시

##### print()

- 데이터를 출력할 수 있는 함수
- 자동적으로 줄 바꿈 발생

```python
print('happy')
print('hacking')
>>> happy
>>> hacking

# 콤마를 사용하면 공백으로 출력
print(a, b)
>>> happy hacking
```

- end, sep 옵션을 사용하여 출력 조작하기

```python
a = 'happy'
b = 'hacking'

# 다 출력되고 마지막에 @
print(a, end='@')
print(b)
>>> happy@hacking

# 구분자, 문자 사이에 개행 \n
print(a, b, sep='\n')
>>> happy
>>> hacking
```

