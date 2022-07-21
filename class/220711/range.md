### 레인지(Range)

- 숫자의 스퀀스를 나타내기 위해 사용
  - 기본형 : range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
  - 범위지정 : range(n, m)
    - n부터 m-1까지의 숫자의 시퀀스
  - 범위 및 스텝 지정 : range(n, m, s)
    - n부터 m-1까지 s만큼 증가시키며 숫자의 스퀀스
- 변경 불가능하며, 반복 가능함
- range는 순자의 시퀀스를 나타내기 위해 사용

```python
range(4) # range(0, 4)
list(range(4)) # [0, 1, 2, 3]
type(range(4)) # <class 'range'>
```

