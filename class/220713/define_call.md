### 선언과 호출

- 함수의 선언은 `def` 키워드를 활용함
- 들여쓰기를 통해 function body를 작성함
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 `return`을 통해 결과 값을 전달함
- 함수는 `함수명()`으로 호출

```python
# 예시
num1 = 0
num2 = 1

def func1(a, b):
    return a+ b

def func2(a, b):
    return a - b

def func3(a, b):
    return func1(a, 5) + func2(5, b)

result = func3(num1, num2)
print(result)
```

