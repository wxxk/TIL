## 딕셔너리

- **키-값 쌍으로 이뤄진 모음**
  - 키 : 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)
  - 값 : 어떠한 형태은 관계 없음
- 키와 값은 : 로 구분 됩니다. 개별 요소는 ,로 구분됩니다.
- 변경 가능하며, 반복 가능합
  - 딕셔너리는 반복하면 키가 반환됩니다.

```python
students = {'홍길동': 30, '김철수': 25}
students['홍길동'] 
# 30
```



- 딕셔너리 생성
  - key와 value가 쌍으로 이뤄진 자료구조
    - key는 변경 불가능한 데이터만 활용
      - string, integer, float, bloolean, tuple, range
    - value는 모든 값으로 설정 가능(List, Dictionary 등)

```python
dict_c = {[1, 2, 3]: 'hi'} 
# key가 List이기 때문에 생성 불가능
```



- 딕셔너리 접근

``` python
movie = {
    'title': '설국열차',
    'genres': ['SF', '액션', '드라마'], #list
    'open_date': '2013-08-01', #str
    'time': 126, #int
    'adult': False, #boolean
} # => value 값은 모든 값 설정 가능

movie['genres'] # => ['SF', '액션', '드라마']

movie['actors'] # => Error
```



- 딕셔너리 키-값 추가 및 변경 (수정)

  - 딕셔너리에 키와 값의 쌍을 추가할 수 있으며,

  - 이미 해당하는 키가 있다면 기존 값이 변경됩니다.

  - 키를 삭제하고자하면 .pop()을 활용하여 삭제하고자 하는 키를 전달

  - 키가 없는 경우 KeyError 발생

```python
# 키-값 추가 및 변경
students = {'홍길동': 100, '김철수': 90}
students['홍길동'] = 80 # {'홍길동': 80, '김철수': 90}
students['박영희'] = 95 # {'홍길동': 80, '김철수': 90, '박영희': 95}

#삭제
students = {'홍길동': 30, '김철수': 25}
students.pop('홍길동')
students # {'김철수': 25}

students = {'홍길동': 30, '김철수': 25}
students.pop('jane')
KeyError: 'jane'
# 키가 없는 경우 KeyError 발생
```
