#### 입력

```python
def function(ham): # parameter
    return ham

function('spam') # argument
```

- parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자

- argument : 함수를 호출할 때 넣어주는 값

  - 함수 호출 시 함수의 parameter를 통해 전달되는 값

  - Argument는 소활호 안에 해당

    - 필수 argument : 반드시 전달되어야 하는 argument 
    - 선택 argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

  - positional arguments : 기본적으로 함수 호출시 argument는 위치에 따라 함수 내에 전달

    ```python
    def add(x, y):
        return x + y
    
    add(2, 3) # positional arguments
    ```

  - keyword arguments : 직접 변수의 이름으로 특정 argument를 전달할 수 있음

    - keyword argument 다음에 positional argument를 활용할 수 없음

    ```python
    def add(x, y):
        return x + y
    
    	add(x=2, y=5) # keyword argument
    ```

  - defalut arguments values

    - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록함

    ```python
    def add(x, y=0)
    	return x + y
    
    add(2)
    ```

    

  - 정해지지 않은 개수의 arguments

    - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
    - 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때 유용

    ```python
    def add (x, y=0)
    	for arg in args:
            print(arg)
            
    # add (2)
    add (2, 3, 4, 5) # 피라미터 수를 정하지 않았으므로, 1개, 2개, 3개 등 모두 가능
    
    # 결과
    (1, 2, 3) #튜플 형식
    ```

    

  - 정해지지 않은 개수의 keyword arguments

    - 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록 지정
    - argument들은 **딕셔너리**로 묶여 처리되며, parameter에 `**`를 붙여 표현

    ```python
    def name_and_age(**kwargs):
    	print(kwargs)
    
    name_and_age(name="홍길동", age="50")
    name_and_age(name="고길동", age="30")
    
    # 결과
    {'name': '홍길동', 'age': '50'}
    {'name': '고길동', 'age': '30'}
    ```

    

