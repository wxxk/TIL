#### 리스트

- 변경가능한 값들의 나열된 자료형
- 순서를 가지며, 서로 다른 타이브이 요소를 가질 수 있음

- 변경 가능하며, 반복가능함
- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분

- 문법

  | 문법                   | 설명                                                         |
  | ---------------------- | ------------------------------------------------------------ |
  | L.append(x)            | 리스트 마지막에 항목 x를 추가                                |
  | L.insert(i, x)         | 리스트 인덱스 i에 항목 x를 삽입                              |
  | L.remove(x)            | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거               |
  | L.pop()                | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
  | L.pop(i)               | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
  | L.extend(m)            | 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은기능)    |
  | L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
  | L.reverse()            | 리스트를 거꾸로 정렬                                         |
  | L.sort()               | 리스트를 정렬 (매개변수 이용가능)                            |
  | L.count(X)             | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환             |

  

  - 값 추가 및 삭제

    - .append(x) : 리스트 마지막에 항목 x 추가

    ```python
    cafe = ['starbucks', 'tomntoms', 'hollys’]
    print(cafe)
    # ['starbucks', 'tomntoms', 'hollys']
    cafe.append('banapresso’)
    print(cafe)
    # ['starbucks', 'tomntoms', 'hollys', 'banapresso']
    ```

    - .extend(**iterable**) : 리스트에 iterable의 항목을 추가함

    ```python
    cafe = ['starbucks', 'tomntoms', 'hollys’]
    print(cafe)
    # ['starbucks', 'tomntoms', 'hollys']
    cafe.extend(['cafe', 'test’])
    print(cafe)
    # ['starbucks', 'tomntoms', 'hollys', 'cafe', 'test]
    ```

    - .insert(i,x) : 정해진 위치 i에 값을 추가함

    ```python
    cafe = ['starbucks', 'tomntoms’]
    print(cafe)
    # ['starbucks', 'tomntoms']
    cafe.insert(0, 'start’)
    print(cafe)
    # ['start', 'starbucks', 'tomntoms'
    ```

    - .remove(x) : 리스트에서 값이 x 인것 삭제

    ```python
    numbers = [1, 2, 3, 'hi’]
    print(numbers)
    # [1, 2, 3, 'hi']
    numbers.remove('hi’)
    print(numbers)
    # [1, 2, 3]
    numbers.remove('hi')
    # ----------------
    # ValueError Traceback (most recent call last)
    ```

    - .pop(i) 
      - 정해진 위치 i에있는 값을 삭제하고, 그 항복을 반환함,
      -  i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

    ```python
    # i 위치 지정되지 않음
    umbers = ['hi', 1, 2, 3]
    # ['hi', 1, 2, 3]
    pop_number = numbers.pop()
    print(pop_number)
    # 3
    print(numbers)
    # ['hi', 1, 2]
    
    # i 위치 정해짐
    numbers = ['hi', 1, 2, 3]
    # ['hi', 1, 2, 3]
    pop_number = numbers.pop(0)
    print(pop_number)
    # 'hi'
    print(numbers)
    # [1, 2, 3]
    ```

    - .clear() : 모든 항목을 삭제

    ```python
    numbers = [1, 2, 3]
    print(numbers)
    # [1, 2, 3]
    print(numbers.clear())
    # []
    ```

  - 탐색 및 정렬

    - .index(x) : x값을 찾아 해당 index 값을 반환

    ```python
    numbers = [1, 2, 3, 4]
    print(numbers)
    # [1, 2, 3, 4]
    print(numbers.index(3))
    # 2
    print(numbers.index(100))
    # ---------------------
    # ValueError Traceback (most recent call last)
    # 2 print(numbers)
    # 3 print(numbers.index(3))
    # ----> 4 print(numbers.index(100))
    # ValueError: 100 is not in list
    ```

    - .count(x) : 원하는 값의 개수를 반환함

    ```python
    numbers = [1, 2, 3, 1, 1]
    print(numbers.count(1))
    # 3
    print(numbers.count(100))
    # 0
    ```

    - .sort() : 원본 리스트를 정렬하고, None 반환(sorted 함수와 비교)

    ```python
    # 원본 변경
    numbers = [3, 2, 5, 1]
    result = numbers.sort()
    print(numbers, result)
    
    #정렬된 리스트 반환. 원본 변경 없음
    umbers = [3, 2, 5, 1]
    result = sorted(numbers)
    print(numbers, result)
    # [3, 2, 5, 1] [1, 2, 3, 5]
    ```

    - .reverse() : 순서를 반대로 뒤집음(정렬하는 것이 아님)

    ```python
    umbers = [3, 2, 5, 1]
    result = numbers.reverse()
    print(numbers, result)
    # [1, 5, 2, 3] None
    ```

