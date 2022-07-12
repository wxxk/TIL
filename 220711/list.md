### 리스트 정의

> 대괄호 ([]) 혹은 list() 를 통해 생성
>
> 값에 대한 접근은 list[i]

- 변경 가능한 값들의 나열된 자료형
- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
  - [1, 'hello', False]
- 변경 가능하며, 반복 가능함
- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분
- 값 추가는 .appen()를 활용하여 추가하고자 하는 값을 전달
- 값 삭제는 .pop()을 활용하여 삭제하고자 하는 인덱스를 전달



- 리스트 생성과 접근

```python
# 생성
my_list = []
another_list = list()
type(my_list) # <class 'list'>
type(another_list) # <class 'list'>


# 접근과 변경
a = [1, 2, 3] # 값 접근
print(a[0]) # 1

a[0] = '1' # 값 변경
print(a) # ['1', 2, 3]


# 추가
even_numbers = [2, 4, 6, 8]
even_numbers.append(10)
even_numbers # => [2, 4, 6, 8, 10]

# 삭제
even_numbers = [2, 4, 6, 8]
even_numbers.pop(0)
even_numbers # => [4, 6, 8]
```

---