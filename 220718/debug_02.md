### 에러 메시지가 발생하는 경우 

- 해당하는 위치를 찾아 메시지를 해결



#### 로직 에러가 발생하는 경우 (결과가 다르게 나오는 경우)

- 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
  - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
  - 전체 코드를 살펴봄 
  - 휴식을 가져봄
  - 누군가에게 설명해봄



#### 문법 에러(syntaxError)

- syntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿 기호(^)를 표시

```python
if else

#-------------------------------------------------------
# File "<ipython-input-1-f8a097d0a658>", line 1 if else ^
# SyntaxError: invalid syntax
```



#### 여러가지 에러들

- EOL (End of Line) - 마침표

```python
print('hello

#-----------------------------------------------------------
# File "C:\Users\dwde2\Desktop\수업연습\0718\실습\00.py", line 1
# print('hello ^
# SyntaxError: EOL while scanning string literal
```

- EOF (End of File ) - 괄호

```python
print(

#------------------------------------------------------------
# File "C:\Users\dwde2\Desktop\수업연습\0718\실습\00.py", line 2 ^
# SyntaxError: unexpected EOF while parsing
```

- invaild syntax - :

```python
while

#-------------------------------------------------------------
# File "C:\Users\dwde2\Desktop\수업연습\0718\실습\00.py", line 1
# while ^
# SyntaxError: invalid syntax
```

- assign to literal - 값을 할당을 할 수 없음(식별자를 잘 만들어야됨)

```python
5 = 3

#-----------------------------------------------------------
# File "C:\Users\dwde2\Desktop\수업연습\0718\실습\00.py", line 1
# 5 = 3 ^
# SyntaxError: cannot assign to literal
```

