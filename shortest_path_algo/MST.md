# 최소 신장 트리(Minimum Spanning Tree)

신장 트리는 무방향 그래프에서 모든 노드를 사이클 없이 잇는 그래프이며, 노드를 잇는 간선의 가중치 합이 최소인 신장 트리를 최소 신장 트리(Minimum Spanning Tree, 이하 MST)라 한다.

## 최소 신장 트리의 대표적인 알고리즘

### 크루스칼(kruskal) 알고리즘

그래프의 간선을 하나씩 늘리며 MST를 만든다. 간선을 늘릴 때 가중치가 최소인 간선부터 추가하는 탐욕법을 이용한다.

**동작 과정**

![크루스칼](images/kruskal.gif)

1. 간선은 가중치를 기준으로 오름차순 정렬한다.

2. 간선을 하나씩 살핀다. 간선을 MST에 추가했을 때 MST에 사이클이 생기지 않으면 추가한다. 사이클이 생긴다면 다음 간선으로 넘어간다.

**특징**

시간 복잡도: O(E log E) - 간선 정렬이 주요 비용  
공간 복잡도: O(V) - Union-Find 자료구조  
희소 그래프(간선이 적은 그래프)에 효율적  
간선 중심의 접근법

### 유니온-파인드(Union-Find) 자료구조

크루스칼 알고리즘에서 **사이클을 효율적으로 판별하기 위해 사용되는 핵심 자료구조**가 바로 **유니온-파인드(Union-Find)**이다.

#### 1) 개념

- **목적**: 어떤 정점들이 동일한 집합(Connected Component)에 속해 있는지를 빠르게 확인하고, 두 정점을 같은 집합으로 합치는 연산을 효율적으로 수행한다.
- **그래프에서의 역할**:
  - 크루스칼 알고리즘에서 간선을 추가할 때, 두 정점이 이미 같은 집합에 속해 있다면 그 간선을 추가하면 사이클이 생긴다.
  - 따라서 두 정점이 같은 집합인지 확인하고, 다르면 합치는 과정이 필요하다.

---

#### 2) 주요 연산

유니온-파인드는 두 가지 핵심 연산으로 구성된다.

- **Find(x)**  
  특정 원소 `x`가 속한 집합의 **대표(루트)**를 찾는 연산이다.  
  모든 원소는 트리 형태로 관리되며, 트리의 루트 노드가 집합의 대표를 나타낸다.

- **Union(x, y)**  
  원소 `x`가 속한 집합과 원소 `y`가 속한 집합을 하나로 합치는 연산이다.  
  합치는 과정에서 한 쪽 트리의 루트를 다른 쪽 트리의 루트에 연결한다.

---

#### 3) 최적화 기법

유니온-파인드는 단순 구현으로도 동작하지만, 트리가 깊어지면 성능이 나빠질 수 있다. 이를 개선하기 위해 두 가지 최적화 기법을 사용한다.

- **경로 압축(Path Compression)**  
  `Find(x)`를 수행할 때, 탐색 경로상의 모든 노드를 루트에 직접 연결하여 트리의 높이를 줄인다.  
  결과적으로 이후 `Find` 호출이 매우 빠르게 수행된다.

- **랭크 기반 합치기(Union by Rank)**  
  `Union(x, y)` 시, 트리의 높이(랭크)가 낮은 트리를 높은 트리 밑에 붙인다.  
  이로 인해 트리의 깊이가 최소화되어 성능이 향상된다.

---

#### 4) 시간 복잡도

유니온-파인드에서 `Find`와 `Union` 연산은 단순 구현 시 최악의 경우 $O(\log n)$ 또는 $O(n)$의 시간이 걸릴 수 있다.  
예를 들어, 모든 원소가 한 줄로 연결된 **편향 트리(Skewed Tree)** 형태가 되면 루트까지 거슬러 올라가는 데 선형 시간이 소요된다.

이를 해결하기 위해 **경로 압축(Path Compression)**과 **랭크 기반 합치기(Union by Rank)** 최적화를 적용한다:

이 두 최적화가 함께 적용되면, 한 번의 연산에 필요한 시간은 상수에 매우 가까워진다.

---

#### 5) 크루스칼에서의 활용

- 간선을 하나씩 검사하면서, 간선이 연결하는 두 정점이 다른 집합에 있다면 MST에 추가하고 집합을 합친다.
- 이미 같은 집합에 속한다면 간선을 추가하면 사이클이 생기므로 건너뛴다.
- 이렇게 해서 MST의 사이클 생성을 효과적으로 방지할 수 있다.

```
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # 랭크 기반 합집합
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal_mst(n, edges):
    """
    크루스칼 알고리즘으로 최소 신장 트리 구하기

    Args:
        n: 정점의 개수
        edges: [(가중치, 정점1, 정점2), ...] 형태의 간선 리스트

    Returns:
        (총 가중치, MST 간선 리스트)
    """
    # 간선을 가중치 순으로 정렬
    edges.sort()

    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):  # 사이클이 생기지 않으면
            mst_edges.append((u, v, weight))
            total_weight += weight

            # MST는 n-1개의 간선을 가짐
            if len(mst_edges) == n - 1:
                break

    return total_weight, mst_edges
```

### 프림(Prim) 알고리즘

그래프의 노드를 하나씩 늘리며 MST를 만든다. 정점을 늘릴 때 정점과 연결된 간선의 가중치가 최소인 것부터 추가하는 탐욕법을 이용한다.

**동작 과정**

![프림](images/prim.gif)

1. 시작 정점을 고른다. 시작 정점을 MST에 추가한다.

2. 정점과 이어진 간선을 살핀다. 간선과 이어진 다음 정점이 MST에 있지 않다면 이 정점과 간선을 최소 힙에 추가한다.

3. 최소 힙에서 꺼낸 정점이 MST에 포함되어 있지 않다면 MST에 추가하고 **2 단계**를 진행한다. 만약 꺼낸 정점이 MST에 포함되어 있으면 넘어간다.

4. 최소 힙이 빌 때까지 **3 단계**를 반복한다.

**특징**

시간 복잡도: O(E log V) - 우선순위 큐 사용 시  
공간 복잡도: O(V) - 방문 배열과 힙  
밀집 그래프(간선이 많은 그래프)에 효율적  
정점 중심의 접근법

```
import heapq
from collections import defaultdict

def prim_mst(n, graph, start=0):
    """
    프림 알고리즘으로 최소 신장 트리 구하기

    Args:
        n: 정점의 개수
        graph: {정점: [(가중치, 인접정점), ...]} 형태의 인접 리스트
        start: 시작 정점 (기본값: 0)

    Returns:
        (총 가중치, MST 간선 리스트)
    """
    visited = [False] * n
    min_heap = [(0, start, -1)]  # (가중치, 현재정점, 부모정점)
    mst_edges = []
    total_weight = 0

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if visited[current]:
            continue

        visited[current] = True
        total_weight += weight

        if parent != -1:  # 시작 정점이 아닌 경우
            mst_edges.append((parent, current, weight))

        # 현재 정점과 연결된 모든 간선을 힙에 추가
        for next_weight, next_vertex in graph[current]:
            if not visited[next_vertex]:
                heapq.heappush(min_heap, (next_weight, next_vertex, current))

    return total_weight, mst_edges

def build_graph_from_edges(edges):
    """간선 리스트로부터 인접 리스트 그래프 생성"""
    graph = defaultdict(list)
    for weight, u, v in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))
    return graph
```

## 최소 신장 트리 활용 분야

- 네트워크 설계 및 인프라 구축: 최소 신장 트리는 통신 네트워크, 전력 그리드, 컴퓨터 네트워크 등의 설계에 널리 사용된다. 최소한의 비용으로 모든 지점을 연결하여 효율적인 네트워크 설계를 가능하게 한다.(DFS, BFS 활용)
- 군집화 알고리즘: 데이터 포인트들 사이의 거리를 기반으로 클러스터를 형성할 때 최소신장트리가 사용될 수 있다. 예를 들어, 머신러닝에서는 MST를 사용하여 데이터를 자연스러운 그룹으로 나누는 데 도움을 준다.
- 회로 설계 및 VLSI(대규모 집적회로) 설계: 전자 회로의 핵심 구성 요소를 연결하는 데 필요한 배선 길이를 최소화하기 위해 MST가 사용된다. 이는 회로의 크기와 비용을 줄이는 데 이바지한다.
- 도로, 파이프라인 및 기타 교통망 설계: 최소 신장 트리는 도로망, 수도 및 가스 파이프라인, 철도망 등의 기반 구축에 있어 총 건설 비용을 최소화하는 데 사용된다.
- 이미지 처리: 이미지의 영역 분할(segmentation)에서 최소 신장 트리를 이용해 이미지의 다른 부분을 구분하기도 한다. 이를 통해 이미지에서 중요한 구조를 식별하고 분석할 수 있다.
- 물류 및 배송: 물류 네트워크에서 각 지점을 최소 비용으로 연결하여 전체 배송 비용을 줄이는 데 활용된다.
