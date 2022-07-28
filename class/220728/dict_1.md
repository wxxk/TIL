### 해시 테이블

- 파이썬에는 딕셔너리 자료구조가 내장 되어 있다. (**Non-sequence** & **Key-Value**)

```python
{
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
# Key는 immutable(변경 불가능)
```

- 해시 함수 : 임의길이의 데이터를 고정 길이의 데이터로 매핑하는 함수

- 해시 : 해시 함수를 통해 얻어진 값

- 특징 : 해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정, 조회 연산의 속도가 리스트 보다 빠르다.



##### 딕셔너리 연산의 시간 복잡도

| 연산 종류   | 시간복잡도 | 리스트         |
| ----------- | ---------- | -------------- |
| Get Item    | O(1)       | O(1)           |
| Insert Item | O(1)       | O(1) 또는 O(N) |
| Update Item | O(1)       | O(1)           |
| Delete Item | O(1)       | O(1) 또는 O(N) |
| Search Item | O(1)       | O(N)           |



##### 딕셔너리는 언제 사용해야할까?

1. 리스트를 사용하기 힘든 경우
2. 데이터에 대한 빠른 접근 탐색이 필요한 경우
3. 현실 세계의 대부분의 데이터가 다른 경우