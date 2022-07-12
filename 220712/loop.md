### 반복문

> 특정 조건을 도달할 때 까지, 계속 반복되는 문장

- while

  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

  - 조건문이 참인경우 반복적으로 코드를 실행

    - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
    - while문은 무한 루프를 하지 않도록 ***종료조건이 반드시 필요***

    ```python
    a = 0
    while a < 5
    	print('a')
        a += 1
    print('끝')
    ```

- for

  > for <변수이름> in <반복가능한>
  >
  > in : 그냥요소 / range(인덱스 접근)

  - 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요없음)

  - 시퀀스를 포함한 순회가능한 객체요소를 모두 순회함

    - 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

    ```python
    for <변수명> in <iterable>:
        # Code blcok
        
    for fruit in ['apple', 'mango', 'banana']:
        print(fruit)
    print('끝')
    # apple
    # mango
    # banana
    ```

  - for문 일반 형식

    - Iterable
      - 순회할 수 있는 자료형(str, list, dict 등)
      - 순회형 함수(range, enumerate)

  - 문자열 순회

    ```python
    chars = input()
    
    for char in chars:
        print(char)
        
    # range를 좀 더 많이 활용
    for idx in range(len(chars)): #chars의 글자 수 만큼 숫자로 만들어준다.
        print(chars[idx])
    ```

  - 딕셔너리 순회

    - 기본적으로 key를 순회하며, key를 통해 값을 활용 (key : value)

      > key가 있으면 value를 가져올 수 있는데,
      >
      > value만 있으면 key를 가져올 수 없음

    ```python
    grades = {'john' : 80, 'eric' : 90}
    for name in grades:
        print(name)
    # john
    # eric
    
    for name in grades:
        print(name, grades[name])
    # john 80
    # eric 90
    ```
