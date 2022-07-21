- #### 기본적인 에러 정리

  - ZerodivisionError : 0으로 나누고자 할 때 발생

  ```python
  10/0
  #-----------------------------------
  # ZeroDivisionError: division by zero
  ```

  - NameError : namespace 상에 이름이 없는 경우(즉, 선언되지 않은 변수일 때 발생)

  ```python
  print(name_error)
  #------------------------------------------
  # NameError: name 'name_error' is not defined
  ```

  - TypeError : 타입 불일치

  ```python
  1 + '1'
  #------------------------------------------------------------
  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
  
  
  round('3.5')
  #--------------------------------------------------
  # TypeError: type str doesn't define __round__ method 
  
  # arguments 부족
  divmod() # 함수호출
  #----------------------------------------------
  # TypeError: divmod expected 2 arguments, got 0
  
  import random # 2개의 위치가 있는데 다 안넣음
  random.sample()
  #----------------------------------------------------------------------------------
  # TypeError: sample() missing 2 required positional arguments: 'population' and 'k'
  
  divmod(1, 2, 3) # 갯수 초과
  #----------------------------------------------
  # TypeError: divmod expected 2 arguments, got 3
  
  import random
  random.sample(range(3), 1, 2)
  #----------------------------------------------------------------------------------
  # TypeError: sample() takes 3 positional arguments but 4 were given
  
  import random
  random.sample(1, 2) # 타입이 다르게 입력
  #-------------------------------------------------------
  # TypeError: Population must be a sequence.  For dicts or sets, use sorted(d).
  ```

  > 읽는 시도와 함께 변수의 이름으로 되어 있을 때 잘 해석 해야함

  

  - valuerError : 타입을 올바르나 값이 적절하지 않은 경우

  ```python 
  int(3.5) # 10진수로 보았을 때 이러한 형태의 문자열은 사용 불가능하다
  # ValueError : invalid literal for int() with base 10: 3.5
  
  --------------------------------------------------------------
  
  range(3).index(6) # 6은 range의 범위 안에 없다
  # ValueError : 6 is not in range
  ```

  - indexerror : 넘어서는 index를 list로 접근하려 했을 때

  ```python
  empty_list = [] #
  empty_list[2]
  # IndexError: list index out of range
  ```

  - keyerror : key가 없어서 발생하는 에러

  ```python
  song = {'IU': '좋은날'}
  song['BTS']
  # KeyError: 'BTS'
  ```

  - moduleNotFoundError : 존재하지 않는 모듈을  import하는 경우

  ```python
  import nonamed
  # ModuleNotFoundError: No module named 'nonamed'
  ```

  - importError : module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우(오타인 경우가 많음)

  ```python
  from random import samp
  # ImportError : connot import name 'samp' from 'random'
  ```

  - indentationError : indentation이 적절하지 않은 경우(space, tap)

  ```python
  for i in range(3)
  print(i)
  # IndentationError: expected an indented block
  ```

  - KeyboardInterrupt - 임의로 프로그램을 종료하였을 때

  ```python
  while True: # 무한히 계속 돌아가는 경우
      continue
  # KeyboradInterrupt:
  ```

  