#### 문자열

- 문자열의 나열 : 모든 타입의 문자 str
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기



- 문자열 탐색

  - .find(x) : x의 첫번째 위치를 반환. 없으면 -1을 반환함.
  - .index(x) : x의 첫 번재 위치를 반환. 없으면, 오류발생
  - .isalpha() : 알파벳 문자여부
  - .isupper() : 대문자 여부
  - .islower() 소문자 여부
  - .istitle() : 타이틀 형식 여부

  ```python
  'apple'.find('p')
  # 1
  
  'apple'.find('k')
  # -1
  ```

  - .index(x) : x의 첫번째 위치를 반환. 없으면 오류 발생

  ```python
  print('apple'.index('p'))
  # 1
  'apple'.index('k')
  # ------------------
  # ValueError Traceback (most recent call last)
  # ----> 1 'apple'. index('k')
  # ValueError 
  ```



- 문자열 관련 검증 메소드

  ```python
  알파뱃 : print ('abc'.isalpha()) # True
  대문자 : print ('Ab'.isupper()) # False
  소문자 : print ('ab'.islower()) # True
  타이틀 : print ('Title Title'.istitle()) # True
  ```

  

**문자열 변경**

- .replace(old, new, [count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

  - count를 지정하면, 해당 개수만큼만 시행

  ```python
  print('coone'.replace('o', 'a')) # caane
  print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
  ```

- .strip([char]) : 공백이나 특정 문자를 제거

  - 양쪽제거(strip), 왼쪽제거(lstrip), 오른쪽제거(rstrip)
  - 문자열을 지정하지 않으면 공백을 제거

  ```python
  print('       와우!\n'.strip()) # '와우!'
  print('       와우!\n'.lstrip()) # '와우!\n'
  print('       와우!\n'.rstrip()) # '       와우!'      
  ```

- .split(sep=None, maxsplit=-1) : 공백이나 특정 문자를 기준을 분리

  - 문자열을 특정한 단위로 나눠 **리스트로 반환**
  - sep이 None이거나 지정되니 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 
  - maxsplit이 -1인 경우에는 제한 없음

  ```python
  print('a,b,c'.split('_')) # ['a,b,c']
  print('a b c'.split()) # ['a', 'b', 'c']
  ```

- 'separator'.join([iterable]) : 구분자로 iterable을 합침

  - 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환

    > iterable에 문자열이 아닌 값이 있으면 TypeError 발생

  ```python
  print(''.join(['3', '5'])) # 35
  ```

- .capitalize() : 가장 첫 번째 글자를 대문자로 변경
- .title() : `'`나 공백 이후를 대문자로 변경
- .upper() : 모두 대문자로 변경
- .lower() : 모두 소문자로 변경
- .swapcase() : 대 - 소문자 서로 변경

