# 목차

1. [그래프란](#그래프란)
   - [수학적 정의](#수학적-정의)
   - [기본 용어](#기본-용어)
2. [그래프의 분류](#그래프의-분류)
   - [1. 방향성에 따른 분류](#1-방향성에-따른-분류)
   - [2. 가중치 유무에 따른 분류](#2-가중치-유무에-따른-분류)
   - [3. 연결성에 따른 분류](#3-연결성에-따른-분류)
   - [4. 특수한 구조에 따른 분류](#4-특수한-구조에-따른-분류)
3. [그래프의 표현 방법](#그래프의-표현-방법)
   - [1. 인접 행렬 (Adjacency Matrix)](#1-인접-행렬-adjacency-matrix)
   - [2. 인접 리스트 (Adjacency List)](#2-인접-리스트-adjacency-list)
   - [3. 간선 리스트 (Edge List)](#3-간선-리스트-edge-list)
   - [표현 방법 비교](#표현-방법-비교)
4. [그래프의 기본 연산](#그래프의-기본-연산)

---

# 그래프란

그래프(G, Graph)는 객체들 사이의 관계를 표현하는 추상적인 자료구조이다. 정점(V, Vertex, 또는 노드(Node))과 이들을 연결하는 간선(E, Edge 또는 Arc)로 구성되어 있다. 정점은 그래프의 기본 구성 요소로, 그래프에서 표현하고자 하는 실제 객체를 나타낸다. 점(Dot)과 같은 개념으로 생각할 수 있다. 간선은 정점들 사이의 관계와 연결을 나타낸다. 선으로 표현되고, 두 정점을 연결한다.

![graph](/assets/graph_concept/graph/graph.png)



## 수학적 정의

다음과 같이 정의된다.

```
G = (V, E)
G : 그래프
V (Vertex set) : 정점 또는 노드들의 집합
E (Edge set) : 간선 또는 호들의 집합
```

## 기본 용어

그래프에서 주로 쓰이는 용어로는 차수(Degree), 경로(Path), 사이클(Cycle)이 있다.

**차수(Degree)**: 정점의 차수는 해당 정점에 연결된 간선의 수를 의미한다. 후에 서술할 방향 그래프에서는 다음과 같이 구분한다.
- **진입 차수(In-degree)**: 정점으로 들어오는 간선의 수
- **진출 차수(Out-degree)**: 정점에서 나가는 간선의 수

![degree](/assets/graph_concept/graph/degree.png)







**경로(Path)**: 정점 u에서 정점 v까지의 경로는 연결된 간선들의 나열이다. 단순 경로(Simple Path)는 같은 정점을 두 번 방문하지 않는 경로이고, 경로의 길이는 경로에 포함된 간선의 수를 의미한다.


**사이클(Cycle)**: 시작 정점과 끝 정점이 같은 경로를 사이클이라 한다. 시작과 끝 정점을 제외하고 같은 정점을 반복하여 방문하지 않는 경우를 단순 사이클, 같은 정점을 반복 방문하는 경우를 비단순 사이클이라 한다.

![path_cycle](/assets/graph_concept/graph/path_cycle.png)



# 그래프의 분류

그래프는 여러 특성에 따라 다양하게 분류할 수 있으며, 각 특성은 독립적으로 적용되어 조합될 수 있다.

## 1. 방향성에 따른 분류

- 무방향 그래프 (Undirected Graph)
무방향 그래프는 간선에 방향이 없는 그래프이다. 간선 (u, v)와 (v, u)는 동일하며, 두 정점 사이의 대칭적 관계를 나타낸다. 무방향 그래프에서 정점의 차수는 해당 정점에 연결된 간선의 수와 같다.

![undirected](/assets/graph_concept/graph/undirected.png)



- 방향 그래프 (Directed Graph)
방향 그래프는 반대로 간선에 방향이 있는 그래프이다. 간선 (u, v)는 정점 u에서 정점 v로의 방향을 가지며, (u, v)와 (v, u)는 서로 다른 간선이다. 방향 그래프에서는 각 정점의 진입 차수와 진출 차수를 구분하여 계산한다.

![directed](/assets/graph_concept/graph/directed.png)



## 2. 가중치 유무에 따른 분류

- 가중 그래프 (Weighted Graph)
가중 그래프는 각 간선에 가중치(비용, 거리, 시간 등)가 부여된 그래프이다. 간선 (u, v)에 가중치 w(u, v)가 할당되어 있으며, 최단 경로 문제나 최소 신장 트리 문제 등에서 핵심적으로 사용된다. 예를 들어, 도시 간 거리나 네트워크에서의 전송 비용을 나타낼 때 활용된다.

![weighted](/assets/graph_concept/graph/weighted.png)


- 비가중 그래프 (Unweighted Graph)
비가중 그래프는 모든 간선의 가중치가 동일하거나 가중치 개념이 없는 그래프이다. 단순히 두 정점 사이의 연결 여부만을 나타내며, 모든 간선의 가중치를 1로 간주할 수 있다. 소셜 네트워크의 친구 관계나 단순한 연결 구조를 표현할 때 사용된다.

![unweighted](/assets/graph_concept/graph/unweighted.png)



## 3. 연결성에 따른 분류

- 연결 그래프 (Connected Graph)
무방향 그래프에서 모든 정점 쌍 사이에 경로가 존재하는 그래프를 연결 그래프라고 한다. 즉, 임의의 두 정점을 선택했을 때 한 정점에서 다른 정점으로 갈 수 있는 경로가 반드시 존재한다. 그래프 탐색 알고리즘에서 모든 정점을 방문할 수 있는지 판단하는 기준이 된다.

![connected](/assets/graph_concept/graph/connected.png)



- 비연결 그래프 (Disconnected Graph)
비연결 그래프는 일부 정점들 사이에 경로가 존재하지 않는 그래프이다. 즉, 그래프가 여러 개의 독립적인 연결 성분으로 나뉘어 있는 상태를 의미한다.

![disconnected](/assets/graph_concept/graph/disconnected.png)



- 강연결 그래프 (Strongly Connected Graph)
강연결 그래프는 방향 그래프에서 모든 정점 쌍 (u, v)에 대해 u에서 v로 가는 경로와 v에서 u로 가는 경로가 모두 존재하는 그래프이다. 즉, 임의의 정점에서 시작하여 다른 모든 정점을 방문하고 다시 시작점으로 돌아올 수 있다. 강연결 성분 분해나 위상 정렬과 밀접한 관련이 있다.

![strongly_connected](/assets/graph_concept/graph/strongly_connected.png)

![SCC](/assets/graph_concept/graph/SCC.png)





## 4. 특수한 구조에 따른 분류

- 완전 그래프 (Complete Graph)
모든 정점 쌍이 간선으로 연결된 그래프이다. n개의 정점을 가진 완전 그래프는 Kₙ으로 표기하며, n(n-1)/2개의 간선을 가진다.

![complete](/assets/graph_concept/graph/complete.png)


- 이분 그래프 (Bipartite Graph)
정점 집합을 두 개의 독립적인 부분집합으로 나눌 수 있고, 모든 간선이 서로 다른 부분집합의 정점들을 연결하는 그래프이다. 같은 부분집합 내의 정점들 사이에는 간선이 존재하지 않는다.

![binary_graph](/assets/graph_concept/graph/binary_graph.png)




- 트리 (Tree)
n개의 정점과 n-1개의 간선을 가지며 사이클이 없는 연결 그래프이다. 임의의 두 정점 사이에 유일한 경로가 존재한다.

![tree](/assets/graph_concept/graph/tree.png)


- 순환 그래프 vs 비순환 그래프 (DAG)
순환 그래프는 하나 이상의 사이클을 포함하는 그래프이고, 비순환 그래프는 사이클이 없는 그래프이다. 특히 방향 그래프에서 사이클이 없는 경우를 DAG(Directed Acyclic Graph)라고 한다.


![DAG](/assets/graph_concept/graph/dag.png)




# 그래프의 표현 방법

그래프를 컴퓨터에서 구현하기 위해서는 적절한 자료구조로 표현해야 한다. 주요한 표현 방법으로는 인접 행렬, 인접 리스트, 간선 리스트가 있다. 하나의 그래프가 있을 때, 컴퓨터에 저장하는 방법이 3가지가 있다고 생각하면 좋다.

## 1. 인접 행렬 (Adjacency Matrix)
n개의 정점을 가진 그래프를 n×n 이차원 배열로 표현하는 방법이다. 배열의 원소 A[i][j]는 정점 i에서 정점 j로의 간선 존재 여부를 나타낸다.

**무방향 그래프**: A[i][j] = A[j][i] = 1 (간선 존재), 0 (간선 없음)
**방향 그래프**: A[i][j] = 1 (i→j 간선 존재), 0 (간선 없음)
**가중 그래프**: A[i][j] = 가중치 값, ∞ 또는 0 (간선 없음)

![adjacency_mat](/assets/graph_concept/graph/adjacency_mat.png)




```python
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # 무방향 그래프의 경우
    
    def is_adjacent(self, u, v):
        return self.graph[u][v] != 0
    
    def get_neighbors(self, vertex):
        neighbors = []
        for i in range(self.V):
            if self.graph[vertex][i] != 0:
                neighbors.append(i)
        return neighbors
```

인접 행렬은 두 정점 간의 인접성 검사가 O(1)에 가능하고 구현이 간단하다는 장점이 있다. 하지만 정점 수에 비례하여 O(V²)의 공간을 사용하므로 희소 그래프에서 공간 낭비가 크다는 단점이 있다.

## 2. 인접 리스트 (Adjacency List)
각 정점에 대해 인접한 정점들의 리스트를 저장하는 방법이다. 배열의 각 원소가 연결 리스트나 동적 배열을 가리킨다.

**무방향 그래프**: 간선 (u, v)가 있으면 u의 리스트에 v를, v의 리스트에 u를 저장
**방향 그래프**: 간선 (u, v)가 있으면 u의 리스트에만 v를 저장
**가중 그래프**: 각 리스트 원소에 (정점, 가중치) 쌍을 저장

![adjacency_list](/assets/graph_concept/graph/adjacency_list.png)


```python
from collections import defaultdict

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # 무방향 그래프의 경우
    
    def is_adjacent(self, u, v):
        for neighbor, _ in self.graph[u]:
            if neighbor == v:
                return True
        return False
    
    def get_neighbors(self, vertex):
        return [neighbor for neighbor, _ in self.graph[vertex]]
```
        

인접 리스트는 실제 간선 수에 비례하여 O(V + E)의 공간을 사용하므로 희소 그래프에 효율적이다. 반면 두 정점 간의 인접성 검사에 O(V)의 시간이 필요할 수 있다는 한계가 있다.

## 3. 간선 리스트 (Edge List)
모든 간선을 하나의 리스트에 저장하는 방법이다. 각 간선을 (u, v) 또는 (u, v, w) 형태로 저장한다.

![edge_list](/assets/graph_concept/graph/edge_list.png)




간선 리스트는 구현이 매우 간단하고 간선 중심의 알고리즘에 적합하다. 다만 특정 정점의 인접 정점을 찾기 위해 전체 리스트를 검사해야 한다는 단점이 있다.

## 표현 방법 비교


| 표현 방법 | 공간 복잡도 | 인접성 검사 | 정점의 모든 인접 정점 찾기 |
|-----------|-------------|-------------|---------------------------|
| 인접 행렬 | O(V²) | O(1) | O(V) |
| 인접 리스트 | O(V + E) | O(V) | O(차수) |
| 간선 리스트 | O(E) | O(E) | O(E) |






