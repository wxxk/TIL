#### 딕셔너리 : 키-값 쌍으로 이루어진 모음

- 키(Key) : 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)

- 값(values) : 어떠한 형태든 관계 없음

- 키와 값은 `:`로 구분. 개별 요소는 `,`로 구분

- 변경 가능하며, 반복 가능

  

- 문법

  | 문법              | 설명                                                         |
  | ----------------- | ------------------------------------------------------------ |
  | d.clear()         | 모든 항목을 제거                                             |
  | d.keys()          | 딕셔너리 d의 모든 키를 담은 뷰를 반환                        |
  | d.values()        | 딕셔너리 d의 모든 값을 담은 뷰를 반환                        |
  | d.items()         | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환                |
  | d.get(k)          | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환 |
  | d.get(k, v)       | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환 |
  | d.pop(k)          | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d 에없을 경우 KeyError를 반환 |
  | d.pop(k, v)       | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d 에없을 경우 v를 반환 |
  | d.update([other]) | 딕셔너리 d의 값을 매핑하여 업데이트                          |

  - 조회 : `.get(key[,default])`
    - key를 통해 value를 가져옴
    - KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본: None)

  ```python
  y_dict = {'apple': '사과', 'banana': '바나나'}
  my_dict['pineapple']
  # ------------------------------
  # KeyError Traceback (most recent call last)
  # 1 my_dict = {'apple': '사과', 'banana': 
  '바나나'}
  # ----> 2 my_dict['pineapple’]
  # KeyError: 'pineapple'
  
  #-------------------------------------------------------
  
  my_dict = {'apple': '사과', 'banana': '바나나'}
  print(my_dict.get('pineapple'))
  # None
  print(my_dict.get('apple'))
  # 사과
  print(my_dict.get('pineapple', 0))
  # 0
  ```

  - 추가 및 삭제 : `.pop(key[,default])`
    - key가 딕셔너리에 있으면 제거하고 해당 값을 반환, 그렇지 않으면 default를 반환
    - default값이 없으면 KeyError

  ```python
  my_dict = {'apple': '사과', 'banana': '바나나'}
  data = my_dict.pop('pineapple')
  print(data, my_dict)
  # ----------------
  # KeyError Traceback (most recent call last)
  # 1 my_dict = {'apple': '사과', 'banana': '바나나'}
  # ----> 2 data = my_dict.pop('pineapple')
  # 3 print(data, my_dict)
  # KeyError: 'pineapple'
  ```

  - 추가 및 삭제 : `update([other])` : 값을 제공하는 key, value로 덮어씁니다.

  ```python
  my_dict = {'apple': '사', 'banana': '바나나'}
  my_dict.update(apple='사과')
  print(my_dict)
  # {‘apple’: ‘사과’, 'banana': '바나나'}
  ```

  

