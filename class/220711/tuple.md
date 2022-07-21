### 튜플

- 정의
  - 불변한 값들의 나열
  - 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
  - 변경 불가능하며, 반복 가능함
  - 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분



- 생성과 접근
  - 소괄호 혹은 tuple()을 통해 생성
  - 값에 대한 접근은 리스트와 동일하게 인덱스로 접근
    - 값 변경은 불가능하여 추가/삭제도 불가능함

```python
# 값 접근
a = (1, 2, 3, 1)
a[1]

# 값 변경 => 불가능
a[1] = '3'
```
