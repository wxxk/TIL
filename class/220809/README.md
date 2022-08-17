# 그래프



### 그래프에 대한 이해

> 정점과 이를 연결하는 간선들의 집합으로 이루어진 비선형 자료구조

- 그래프 관련 용어
  - 정점(Vertex) : 간선으로 연결되는 객체이며, 노드(Node)라고도 한다.
  - 간선(Edge) : 정점 간의 관계(연결)를 표현하는 건을 의미한다.
  - 경로(Path) : 시작 정점부터 도착 정점까지 거치는 정점을 나열하는 것을 의미
  - 인접(Adjacency) : 두 개의 정점이 하나의 간선을 직접 연결된 상태를 의미



### 그래프의 종류

1. ##### 무방향 그래프

   - 간선의 방향이 없는 가장 일반적인 그래프
   - 간선을 통해 양방향의 정점 이동 가능
   - 차수(Degree) : 하나의 정점에 연결된 간선의 개수
   - 모든 정점의 차수의 합 = 간선 수 * 2



2. ##### 유방향 그래프

   - 간선의 방향이 있는 그래프
   - 간선의 방향이 가라키는 정점으로 이동가능
   - 차수 : 진입 차수와 진출 차수로 나누어짐
     - 진입 차수 : 외부 정점에서 한 정점으로 들어오는 간선의 수
     - 진출 차수 : 한 정점에서 외부 정점으로 나가는 간선의 수



### 그래프의 표현

1. ##### 인접 행렬

> 두 정점을 연결하는 간선이 없으면 0, 있으면 1을 가지는 행렬로 표시하는 방식

```python
edges = [
    [1, 2],
    [1, 2],
    [1, 4],
    [2, 4],
    [3, 4]
]

# 인접 행렬 만들기

n = 7 # 정점 개수
m = 7 # 간선 개수

graph = [[0] * n for _ in range(n)]

for _ in inrage(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

'''
graph = [
[0, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 1, 1, 0, 0],
[1, 0, 0, 0, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0]
'''
```



2. ##### 인접 리스트

> 리스트를 통해 각 정점에 대한 인접 정점들을 순차적으로 표현하는 방식

```python
# 인접 리스트 만들기

n = 7
m = 7

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
'''
graph = [
[1, 2],
[0, 3, 4],
[0, 4, 5],
[1],
[1, 2, 6],
[2],
[4]
]'''
```



##### 인접 행렬 vs 인접 리스트

- 인접 행렬은 직관적이고 만들기 편하지만, 불필요하게 공간이 낭비된다.
- 인접 리스트는 연결된 정점만 저장하여 효율적이므로 자주 사용된다.