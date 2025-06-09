# 위상 정렬 (Topological Sort)

## 목차
1. [실생활 예시: 선수 과목](#실생활-예시-선수-과목)
2. [위상 정렬이란?](#위상-정렬이란)
3. [구현의 편의를 위한 성질](#구현의-편의를-위한-성질)
4. [알고리즘 구현](#알고리즘-구현)
5. [위상 정렬 수행 예시 (단계별)](#위상-정렬-수행-예시-단계별)
6. [파이썬코드](#파이썬-코드)

---
## 실생활 예시: 선수 과목

위상정렬을 설명하기 위해 간단한 예시를 들어보겠다.

실생활에서 쉽게 볼 수 있는 예로, 교과 이수 제도가 있다.

대학교에서는 선수 과목(prerequisite subjects)이 정해져 있어 어떤 과목을 듣기 전에 반드시 먼저 들어야 하는 과목들이 있다.

![선수과목.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/선수과목.png)

프로그래밍 1을 무조건 들어야만 프로그래밍2, 자료구조를 들을 수 있다.

프로그래밍1을  안듣고 객체지향 프로그래밍을 수강할 수 없다.

![위상정렬예시1.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬예시1.png)


123456, 135426 등 여러가지 정렬이 나올 수 있다.

하지만 35146등 3이 1보다 먼저 나오는 정렬은 잘못된 정렬 이다.

---
## 위상 정렬이란?

방향 그래프에서 간선으로 주어진 정점 간 **선후 관계를 위배하지 않도록 정렬**하는 것이다.  

위상정렬이란? 방향 그래프에서 간선으로 주어진 정점 간 선후 관계를 위배하지 않도록 나열하는 정렬 하는 것이다.


![위상정렬_사이클.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬_사이클.png)

그래프 내에 사이클이 존재할 경우에는 올바른 위상정렬이 존재할 수 없다. 선후관계를 위배한다.

![위상정렬본문예시1.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시1.png)

위상 정렬 상에서 제일 앞에 오는 원소가 무엇인지 정해봅시다.

제일 앞에 오기 위해서는 자신보다 앞에 위치해야 하는 정점이 하나도 없어야한다.

이 말의 즉슨 자신에게 들어오는 간선이 없어야한다. (indegree = 0)

![위상정렬본문예시2.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시2.png)

A, G, C가 가능한 후보군임을 알 수 있다.

셋 중 어느 것이 제일 앞에 오더라도 전혀 상관이 없겠지만 A를 선택 하겠다.

![위상정렬본문예시3.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시3.png)

일단 A를 위상 정렬의 제일 앞에 위치시켰다. 이제 위상 정렬을 계속 진행하기 위해 A에서 나가는 간선을 살펴야 한다. 주어진 그래프에서는 A에서 B로 가는 간선만 존재한다. 이 간선은 A가 B보다 먼저 나와야 한다는 제약 조건을 의미한다. 그런데 이미 A가 위상 정렬에 포함되었으므로 이 제약 조건은 자연스럽게 충족된다. 즉, A를 위상 정렬에 추가한 이후에는 A에서 나가는 간선이 더 이상 제약 조건으로 작용하지 않는다.

![위상정렬본문예시4.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시4.png)
![위상정렬본문예시5.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시5.png)

C가 제거 된 후 B,D,E,F,G로 이루어진 그래프에서 제일 앞에 위치할 수 있는 정점은 D, G 이다. C가 사라지면서 D가 새롭게 추가 되었다.

임의로 D를 선택하겠다.

![위상정렬본문예시6.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시6.png)

정점 D가 제거된 후 그래프가 분리되었다. 분리된 것은 신경 쓰지 않고 과정을 이어가겠다. B, E, F, G로 이루어진 그래프에서 제일 앞에 위치할 수 있는 정점은 B와 G이다. 임의로 G를 선택하겠다.

![위상정렬본문예시7.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시7.png)

E를 제거 해보겠다.

![위상정렬본문예시8.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시8.png)

순서대로 B와 F를 삭제 해보겠다.

![위상정렬본문예시9.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시9.png)

![위상정렬본문예시10.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬본문예시10.png)

주어진 그래프에서 위상 정렬이 완료되었다. 매 순간 들어오는 간선이 없는 정점을 제거하는 방식으로 위상 정렬을 구현할 수 있다.

---
### 구현의 편의를 위한 성질

1. 정점과 간선을 실제로 지우지 않고 미리 indegree 값을 저장한 뒤, 뻗어나가는 정점들의 indegree 값만 1씩 감소시키면서 과정을 수행할 수 있다.
2. indegree가 0인 정점을 매번 모든 정점에서 찾는 대신, 목록을 따로 관리하여 직전에 제거한 정점과 연결된 정점들만 목록에 추가한다. 이 목록은 큐로 관리하며, 큐 대신 배열이나 스택을 사용해도 무방하다.

위 구현을 보면 정점과 간선을 지우고, indegree가 0인 정점을 찾는 과정이 복잡해 보인다. 이 과정을 그대로 구현하면 대부분 O(V²) 시간복잡도를 가진 코드가 되기 쉽다. 하지만 몇 가지 성질을 잘 활용하면 훨씬 간단하게 O(V+E)의 효율적인 시간복잡도로 구현할 수 있다.

---
### 알고리즘 구현
1. 맨 처음 모든 간선을 읽으며 indegree 테이블을 채운다
2. indegree가 0인 정점들을 모두 큐에 넣는다.
3. 큐에서 정점을 꺼내어 위상 정렬 결과에 추가한다.
4. 해당 정점으로부터 연결된 모든 정점의 indegree 값을 1 감소시킨다. 이 때 indegree가 0이 되었다면 그 정점을 큐에 추가한다.
5. 큐가 빌 때까지 3,4번 과정을 반복한다.

---
### 위상 정렬 수행 예시 

![위상정렬수행예시1.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시1.png)

indegree 배열을 모두 채운 후, indegree가 0인 정점들을 큐에 넣는다. 이때 BFS나 DFS에서 하던 방문 체크는 필요 없다. 왜냐하면 앞으로 indegree가 0이 될 때만 큐에 넣는데, 각 정점의 indegree가 0이 되는 순간은 정확히 한 번뿐이기 때문이다.

큐의 front에 있는 정점 A를 꺼내 위상 정렬 결과에 추가한다. 실제로 정점 A와 A에서 B로 가는 간선을 지우는 대신, 정점 A를 관념적으로 제거한다. 그에 따라 A와 연결된 정점 B의 indegree가 1 감소한다. 아직 B의 indegree가 0이 아니므로 큐에 넣지 않는다.

![위상정렬수행예시2.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시2.png)

큐의 front에 있는 A를 꺼내 위상 정렬 결과에 추가한다. 실제로 정점 A와 A에서 B로 가는 간선을 지우는 대신, 정점 A를 관념적으로 제거하여 A와 연결된 정점 B의 indegree를 1 감소시킨다. 정점 B의 indegree가 아직 0이 아니므로 큐에 넣지 않는다.

![위상정렬수행예시3.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시3.png)

큐의 front에 있는 C를 꺼내 위상 정렬 결과에 추가한다. 정점 C를 관념적으로 제거하므로 C에서 연결된 정점 B와 D의 indegree를 1 감소시킨다. 정점 B의 indegree는 아직 0이 아니어서 큐에 넣지 않고, 정점 D의 indegree는 0이 되어 큐에 추가한다.

![위상정렬수행예시4.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시4.png)

큐의 front에 있는 G를 꺼내 위상 정렬 결과에 추가한다. 정점 G를 관념적으로 제거하므로 G에서 연결된 정점 E의 indegree를 1 감소시킨다. 정점 E의 indegree는 아직 0이 아니어서 큐에 넣지 않는다.

![위상정렬수행예시5.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시5.png)

큐의 front에 있는 D를 꺼내 위상 정렬 결과에 추가한다. 정점 D를 관념적으로 제거하므로 D에서 연결된 정점 B와 E의 indegree를 각각 1 감소시킨다. 정점 B와 E의 indegree가 모두 0이 되어 큐에 추가한다.

![위상정렬수행예시6.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시6.png)

큐의 front에 있는 B를 가져와 위상 정렬 결과에 추가한다. 정점 B를 관념적으로 지울 것인데 B로부터 연결된 정점이 없으므로 indegree의 값은 변화하지 않는다.

![위상정렬수행예시7.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시7.png)

큐의 front에 있는 E를 가져와 위상 정렬 결과에 추가한다. 정점 E를 관념적으로 지울 것이기 때문에 E로부터 연결된 정점 F의 indegree가 1 감소한다. 정점 F의 indegree는 0이기 때문에 큐에 추가한다.

![위상정렬수행예시8.png](/graph_algo/assets/ch10_graph_algo/topological_sorting/위상정렬수행예시8.png)

큐의 front에 있는 F를 가져와 위상 정렬 결과에 추가한다. 정점 F를 관념적으로 지울 것인데 F로부터 연결된 정점이 없으므로 indegree의 값은 변화하지 않는다. 이제는 큐가 비었기 떄문에 위상 정렬이 종료된다. 위상 정렬 결과를 확인해보면 위상 정렬이 잘 수행되었음을 알 수 있다.

---
## 파이썬 코드

```python
from collections import deque

# 예시 그래프 (0번부터 시작)
adj = [[] for _ in range(10)]  # 인접 리스트
deg = [0] * 10                 # 진입 차수
n = 0                          # 노드 개수

# 예시 초기화
n = 6
edges = [(1, 2), (1, 3), (3, 4), (5, 6)]
for u, v in edges:
    adj[u].append(v)
    deg[v] += 1

q = deque()
result = []

# 진입 차수가 0인 노드를 큐에 넣기
for i in range(1, n + 1):
    if deg[i] == 0:
        q.append(i)

# 위상 정렬
while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in adj[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            q.append(nxt)

# 사이클 존재 여부 확인
if len(result) != n:
    print("cycle exists")
else:
    print("Topological Sort Result:")
    print(*result)

```

우선 N개의 정점이 있으며, 번호는 1부터 시작한다. adj에는 해당 정점에서 뻗어나가는 정점들의 목록이 저장되어 있다. 이는 방향 그래프에서 인접 리스트를 이용한 그래프 저장 방식이다. 그리고 deg에는 각 정점의 indegree 값이 저장되어 있다.

이 알고리즘의 시간복잡도를 고려하면, 각 정점은 큐에 최대 1번 들어가고, indegree를 감소시키는 연산은 각 간선에 대해 딱 1번만 발생한다. 따라서 시간복잡도는 O(V+E)이다. 이는 그래프에서 BFS나 DFS가 O(V+E)인 것과 같은 맥락이다.

큐의 front에 있는 G를 꺼내 위상 정렬 결과에 추가한다. 정점 G를 관념적으로 제거하므로 G에서 연결된 정점 E의 indegree를 1 감소시킨다. 정점 E의 indegree는 아직 0이 아니어서 큐에 넣지 않는다.

---
### 참고
- 참고한 자료
    - https://blog.encrypted.gg/1020
- 이미지
    - @h__goose
- 추가로 참고하면 좋은 자료
    - Do it 알고리즘
    - 이것이 코딩 테스트다