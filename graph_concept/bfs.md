# 너비 우선 탐색(Breadth-First Search, BFS)

## 📚 목차

1. [1. 너비 우선 탐색(Breadth-First Search, BFS)](#1-너비-우선-탐색breadth-first-search-bfs)
2. [2. BFS는 어떻게 동작하는가](#2-bfs는-어떻게-동작하는가)
3. [3. 예시: 무방향 그래프 탐색](#3-예시-무방향-그래프-탐색)
4. [4. BFS가 왜 최단 거리 탐색에 좋은가](#4-bfs가-왜-최단-거리-탐색에-좋은가)
5. [5. 최단 경로를 출력하려면?](#5-최단-경로를-출력하려면)
6. [6. BFS가 만든 너비 우선 트리](#6-bfs가-만든-너비-우선-트리)
7. [7. BFS는 어디에 쓰이는가](#7-bfs는-어디에-쓰이는가)
   - [7-1. 미로 탐색](#7-1-미로-탐색)
   - [7-2. 최단 거리 계산](#7-2-최단-거리-계산)
8. [8. 벨만-포드 알고리즘(Bellman-Ford Algorithm)](#8-벨만-포드-알고리즘bellman-ford-algorithm)
   - [8-1. 어떤 문제를 풀 수 있는가](#8-1-어떤-문제를-풀-수-있는가)
   - [8-2. 동작 원리](#8-2-동작-원리)
   - [8-3. 구현 코드](#8-3-구현-코드)
   - [8-4. 예시](#8-4-예시)
9. [9. 정리](#9-정리)
10. [10. 참고](#10-참고)

---

## 1. 너비 우선 탐색(Breadth-First Search, BFS)

너비 우선 탐색(BFS)은 그래프나 트리에서 **가장 가까운 곳부터 차례로 탐색하는 방법**이다.  
시작 노드에서부터 인접한 노드를 먼저 모두 방문하고, 그 다음으로 먼 노드를 방문한다.  
이 방식은 **최단 거리 계산**, **레벨 순회** 등에 사용된다.

## 2. BFS는 어떻게 동작하는가

BFS는 **큐(Queue)** 라는 자료구조를 이용한다.  
먼저 시작 노드를 큐에 넣고, 큐에서 하나씩 꺼내면서 그 노드와 연결된 이웃 노드를 차례로 방문해 큐에 넣는다.  
방문 여부를 체크해 중복 방문을 막는다.

```python
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)  # 방문 여부 리스트
    queue = deque()

    visited[start] = True  # 시작 노드 방문 처리
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
```

## 3. 예시: 무방향 그래프 탐색

```python
graph = [
    [],         # 0번 노드는 사용하지 않음
    [2, 3, 4],  # 1번 노드는 2, 3, 4와 연결됨
    [1, 4],     # 2번 노드는 1, 4와 연결됨
    [1, 4],     # 3번 노드는 1, 4와 연결됨
    [1, 2, 3],  # 4번 노드는 1, 2, 3과 연결됨
]

bfs(graph, 1)  # 출력: 1 2 3 4
```

## 4. BFS가 왜 최단 거리 탐색에 좋은가

### 4-1. 실제 최단 거리보다 작게 나올 일은 없다

모든 정점 `v`에 대해:

```
계산된 거리 v.d >= 실제 최단 거리 δ(s, v)
```

- 여기서 v.d는 BFS가 계산한 시작점 s에서 정점 v까지의 거리(탐색 과정에서 기록된 거리)이고,
- 𝛿(𝑠,𝑣)-δ(s,v)는 실제로 존재하는 s에서 v까지의 진짜 최단 거리이다.

즉, 거리가 줄어드는 경우는 없고, 정답이거나 더 큰 값이다.

### 4-2. 큐에 들어가는 순서는 거리 기준으로 정렬되어 있다

- 큐에 들어있는 정점들을 살펴보면, 앞쪽 정점이 항상 더 가까운 노드이다.
- 그래서 다음에 방문할 노드는 지금까지 본 것보다 멀리 있는 노드이다.

즉, BFS는 출발점으로부터 모든 노드까지의 최단 거리를 정확히 계산한다.

## 5. 최단 경로를 출력하려면?

아래 함수는 `predecessor` 배열을 사용해 시작점부터 도착점까지 경로를 재귀적으로 출력한다.

```python
def print_path(predecessor, start, v):
    if v == start:
        print(start, end=' ')
    elif predecessor[v] is None:
        print("경로가 존재하지 않습니다")
    else:
        print_path(predecessor, start, predecessor[v])
        print(v, end=' ')
```

## 6. BFS가 만든 너비 우선 트리

BFS는 각 노드가 어떤 노드를 통해 방문됐는지 기록한다.  
이걸 기반으로 **너비 우선 트리**가 만들어지는데,  
이는 시작점에서 모든 도달 가능한 노드를 **최단 경로로 연결한 트리**이다.

## 7. BFS는 어디에 쓰이는가

### 7-1. 미로 탐색

2차원 배열로 된 미로에서 출발점부터 도착점까지 가장 짧은 경로를 찾을 수 있다.  
BFS는 한 칸씩 사방으로 퍼져 나가기 때문에 최단 거리를 보장한다.

### 7-2. 최단 거리 계산

모든 간선의 가중치가 1이라면, 아래처럼 간단하게 최단 거리도 구할 수 있다.

```python
def shortest_path(graph, start):
    from collections import deque
    distance = [-1] * len(graph)  # -1은 아직 방문하지 않음
    queue = deque()

    distance[start] = 0
    queue.append(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance
```

## 8. 벨만-포드 알고리즘(Bellman-Ford Algorithm)

BFS는 간선의 가중치가 모두 같을 때 사용하기 좋다.  
하지만 간선의 가중치가 음수일 경우엔 사용할 수 없다.  
왜냐하면 어떤 노드에서 음수 간선을 지나면 실제 최단 거리가 줄어드는데, BFS 는 큐에 넣은순서대로 노드를 방문해서 이미 방문한 노드를 다시 방문하지 않기 때문이다.
이 경우에는 **벨만-포드 알고리즘**을 사용한다.

### 8-1. 어떤 문제를 풀 수 있는가

- 그래프에 **음수 가중치**가 있어도 최단 경로를 찾을 수 있다.
- 또한 **음수 사이클**이 존재하는지도 판단할 수 있다.

### 8-2. 동작 원리

- 모든 간선을 **V-1번** 반복해서 점검하며, 더 짧은 경로가 있으면 갱신한다.
- 마지막에 한 번 더 점검해서 갱신되는 간선이 있다면 **음수 사이클이 존재**한다.

### 8-3. 구현 코드

```python
def bellman_ford(edges, vertex_count, start):
    INF = float('inf')
    distance = [INF] * vertex_count
    distance[start] = 0

    for _ in range(vertex_count - 1):
        for u, v, weight in edges:
            if distance[u] != INF and distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight

    # 음수 사이클 확인
    for u, v, weight in edges:
        if distance[u] != INF and distance[v] > distance[u] + weight:
            return None  # 음수 사이클 존재

    return distance
```

### 8-4. 예시

```python
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
]

distance = bellman_ford(edges, 4, 0)

if distance is None:
    print("음수 사이클이 존재한다.")
else:
    print(distance)
# 출력: [0, 4, 1, 5]
```

## 9. 정리

| 알고리즘           | 특징                                      | 시간 복잡도  | 음수 간선 허용 |
| ------------------ | ----------------------------------------- | ------------ | -------------- |
| BFS                | 가까운 노드부터 탐색, 최단 거리 계산 가능 | \$O(V + E)\$ | 안 됨          |
| 벨만-포드 알고리즘 | 음수 간선 허용, 음수 사이클 탐지 가능     | \$O(VE)\$    | 가능           |

## 10. 참고
