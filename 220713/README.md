# 함수

### 목차

- [정의](README.md)
- 함수 기본 구조
  - [선언과 호출](define_call.md)
  - [입력](input.md)
  - [범위](scope.md)
  - [결과값](output.md)
- [함수 응용](apply.md)



### 정의

- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용
  - [파이썬 레퍼런스](https://docs.python.org/ko/3/library/index.html)
  - [파이썬 튜토리얼](https://docs.python.org/ko/3/tutorial/index.html)

- 사용자함수
  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

```python
def function_name
	# code block
    return returning_value
```

- 함수를 사용해야 하는 이유
  - 코드 중복 방지
  - 재사용 용이

```python
values = [100, 75, 85, 90, 65, 95]
total = 0
cnt = 0

for value in values:
	total += value
	cnt += 1
mean = total / cnt

total_var = 0
for value in values:
	total_var += (value - mean) ** 2
    
sum_var = total_var / cnt
target = sum_var

while True:
	root = 0.5 * (target + (sum_var/target))
	if (abs(root - target) < 0.00000000001):
		break
	target = root
    
std_dev = target
print(std_dev)
```

```python
# 내장함수 활용
import math
values = [100, 75, 85, 90, 65, 95]
mean = sum(values) / len(values)
sum_var = sum(pow(value - mean, 2) for value in values) / len(values)
std_dev = math.sqrt(sum_var)
print(std_dev)
```

```python
# pstdev 함수
import statistics
values = [100, 75, 85, 90, 65, 95]
statistics.pstdev(values)
```

