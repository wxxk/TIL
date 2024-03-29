# 완전 탐색



### 무식하게 풀기 (Brute-force)

> 모든 경우의 수를 탐색하여 문제를 해결하는 방식
>
> BOJ_2798 블랙잭

- 브루트포스 (Brute-force)라고도 하며, 무식하게 밀어붙인다는 뜻
- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해서 풀 수 있다.
- 복잡한 알고리즘보다는, 아이디어를 어떻게 코드로 구현할 것인지가 중요.



### 델타 탐색 (Delta Search)

> 이차원 리스트의 모든 원소를 순회 (완전탐색)하며, 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식

- 이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색을 한다. 
- 이때 행과 열의 변량인 -1, +1을 델타(delta)값 이라 한다.

```python
# 행을 x, 열 y로 표현
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 행을 r, 열을 c로 표현
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 튜플로 사용하기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

----------------------------------------------
# 1. 델타값 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2. 이차원 리스트 순회
for x in range(n):
    for y in rnage(m)
    
    # 3. 델타값을 이용해 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 4. 범위를 벗어나지 않으면 갱신
        if 0 <= nx < x and 0 <= ny < m:
            x = nx
            y = ny
```