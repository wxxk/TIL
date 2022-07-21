### 변수

> - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름
>   - 객체 : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것
> - 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에, 즉 참조하는 객체가 바뀔 수 있기 때문에 '변수' 라고 불림

- 변수는 할당 연산자 (=)를 통해 값을 할당

- type()

  - 변수에 할당된 값의 타입

- id()

  - 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소 (* 이후, 자세히 다룰 예정)

- 같은 값을 동시에 할당할 수 있음

  ```python
  x = y = 1004
  print(x, y)
  ```

- 다른 값을 동시에 할당 할 수 있음

  ```python
  x, y = 1, 2
  print(x, y)
  ```

- 실습 문제

  - x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하시오.

    ```python
    # 임시 변수 활용
    tmp = x
    x = y
    y = tmp
    print (x, y)
    
    # pythonic!
    y, x = x, y
    print(x, y)
    ```

-  파이썬 객체를 식별하는데 사용하는 이름

- 규칙

  - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

  - 첫 글자에 숫자가 올 수 없음

  - 길이제한이 없고, 대소문자를 구별

  - 다음의 키워는 예약어로 사용할 수 없음

    | False, None, True, and, as ,assert, async, await, break, class, continue, def, del, dlif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield |
    | ------------------------------------------------------------ |

  - 키워드 / 예약어 확인

    ```python
    import keyword
    print(keyword.kwlist)
    ```

  - 내장함수나 모듈 등의 이름으로도 만들면 안됨
    - 기존의 이름에 다른 값을 할당하게 되므로 더 이상 작동하지 않음

- 사용자 입력

  - input([prompt])

    - 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

    - 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음

    - **반환값은 항상 문자열의 형태로 반환**

      ```python
      name = input('이름을 입력해주세요 : ')
      print(name)
      # 이름을 입력해주세요 : 파이썬
      type(name)
      # str
      ```