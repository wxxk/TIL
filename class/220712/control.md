### 반복 제어

- break : 반복문을 종료

```python
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
# 0
# 1
# 2
    
    
for i in range(10):
    if i > 1:
        print('0과 1만 필요해!')
        break
    print(i)
# 0
# 1
# 0과 1만 필요해!
```



- continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# 1
# 3
# 5
```



- for-else : 끝까지 반복문을 실행한 이후에 else문 실행
  - break를 통해 중간에 종료되는 경우 else 문은 실행 되지 않음

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b'가 없습니다.)
# b가 없습니다.
    
    
for char in 'banana':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')
# b!
```

