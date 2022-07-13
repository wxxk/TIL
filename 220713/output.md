### 결과값

- 함수는 반드시 값을 **하나만** return한다.
  - 명시적인 return이 없는 경우에도 None을 반환한다
  - 함수는 return과 동시에 실행이 종료됩니다.

```python
def foo():
    return '' # 하나의 값만 return하고 함수 실행이 종료
	return '' # 도달할 수 없는 코드
```

- 튜플 반환

```python
# return문을 한번만 사용하면서 두 개 이상의 값을 반환하는 방법
def minus_and_product(x, y):
    return x - y, x * y

result = minus_and_product(4, 5)
print(result, type(result))
# 두개의 값이 아니라 하나의 튜플만 반환됨
```

- return vs print

  - return은 함수 안에서 값을 반환하기 위해 사용되는 키워드

  - print는 출력을 위해 사용되는 함수

