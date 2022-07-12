### 조건문

#### 조건문 기본

- 참/거짓을 판단할 수 있는 조건식과 함께 사용



- 기본형식

  > expression에는 참/거짓에 대한 조건식
  >
  > > 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행
  > >
  > > 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행
  > >
  > > > else는 선택적으로 활용 가능함

  ```python
  if < experssion > :
      # Run this Code block (참일 때 실행)
  else:
      # Run this Code block (거짓일 때 실행)
  
  a = 10 
  if a >= 0;
  	print('양수')
  else:
      print('음수')
  print(a)
  ```

- 복수 조건문

  > 복수의 조건실을 활용할 경우 elif를 활용하여 표현함

  ```python
  if <expression>:
      # Code block
  elif <expression>:
      # Code block
  elif <expression>:
      # Code block
  else <expression>:
      # code block
  ```

- 중첩 조건문

  > 조건문은 다른 조건문에 중첩되어 사용될 수 있음
  >
  > > 들여쓰기를 유의하여 작성할 것

  ```python
  if <expression>:
      # Code block
      if <expression>:
          # Code block
  ```

- 조건 표현식

  > 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

  - 삼항 연산자

  ```python
  value = num if num >= 0 else - num
  ```

  - 예시

  ```python
  num = 2
  if num % 2:
      result = '홀'
  else:
      result = '짝'
  print(result)
  
  # 위 아래 동일
  
  num = 2
  result = '홀' if num % 2 else result = '짝'
  print(result)
  ```

  