# BFS (Breadth-First Search) 알고리즘

## 핵심 개념

- 정의: BFS는 그래프에서 시작 정점으로부터 인접한 정점들을 먼저 방문하며 점차 너비 방향으로 확장해 나가는 탐색 알고리즘이다.
- 적용 대상: 무방향 그래프, 방향 그래프 모두 사용 가능하다.
- 사용 목적:
  - 그래프 탐색
  - 최단 거리 계산 (비가중치 그래프)
  - 연결 요소 확인

## 동작 원리

1. 시작 정점을 큐에 삽입하고 방문 처리한다.
2. 큐에서 정점을 하나씩 꺼내면서 인접 정점들을 확인한다.
3. 아직 방문하지 않은 인접 정점을 큐에 추가하고 방문 처리한다.
4. 큐가 빌 때까지 위 과정을 반복한다.

이 방식은 그래프에서 최단 경로 트리(shortest-path tree)를 구성할 수 있도록 한다. 이를 위해 각 정점의 distance와 predecessor를 관리한다.

## Python 구현 예시

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        u = queue.popleft()
        print(u, end=' ')
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

# 인접 리스트로 표현된 예제 그래프
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
```

### 출력 결과

```
A B C D E F
```

## 시간 및 공간 복잡도

- 시간 복잡도: O(V + E)
  - V: 정점 수, E: 간선 수
- 공간 복잡도: O(V)
  - 큐와 방문 집합이 필요하다

## 활용 사례

- 비가중치 그래프에서 최단 경로 계산
- 미로에서 최단 거리 탐색
- 소셜 네트워크에서 연결 관계 분석
- 웹 크롤러 구현

## DFS와의 비교

| 비교 항목      | BFS                    | DFS                         |
| -------------- | ---------------------- | --------------------------- |
| 탐색 방식      | 너비 우선              | 깊이 우선                   |
| 자료 구조      | 큐 (Queue)             | 스택 (Stack) 또는 재귀 호출 |
| 최단 거리 보장 | 가능 (비가중치 그래프) | 불가능                      |
| 메모리 사용량  | 높을 수 있음           | 비교적 낮음                 |

## 정리

BFS는 단순한 알고리즘이지만 실용적인 응용 범위가 넓다. 특히 최단 거리 문제에서 자주 사용되며, DFS와 함께 그래프 탐색의 기본 알고리즘으로 활용된다. 실제 문제 해결 시 문제의 특성에 따라 적절히 선택해야 한다.

## 참고 문헌

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press. (Chapter 20.2)
