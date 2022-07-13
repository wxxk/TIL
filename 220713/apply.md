### 함수 응용

- 파이썬 인터프리터에는 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음
- ​	map(funcion, iterable)
  - **순회 가능한** 데이터구조의 모든 요소에 함수적용하고, 그 결과를 map object로 반환

```python
n, m = map(int, input().split())
#3, 5

print(n, type(n))
print(m, type(m))

# 3 <class 'int'>
# 5 <class 'int'>
```

