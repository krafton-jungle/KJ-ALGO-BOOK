# 벨만-포드(Bellman-Ford) 알고리즘 완벽 가이드

## 📚 목차

1. [벨만-포드 알고리즘이란?](#1-벨만-포드-알고리즘이란)
2. [알고리즘 원리](#2-알고리즘-원리)
3. [구현 방법](#3-구현-방법)
4. [장단점 분석](#4-장단점-분석)
5. [시간복잡도 분석](#5-시간복잡도-분석)
6. [결론](#6-결론)
7. [참고](#7-참고)

---

## 1. 벨만-포드 알고리즘이란?

**벨만-포드(Bellman-Ford) 알고리즘**은 **음의 가중치가 허용되는** 최단 경로 알고리즘이다.  

다익스트라 알고리즘과는 달리 **음의 가중치 간선**이 있어도 동작한다.

- 단일 시작점에서 **모든 정점까지 최단 거리**를 계산한다.
- 음의 사이클이 있는 경우 탐지 후 예외를 반환한다.

---

## 2. 알고리즘 원리

벨만-포드는 **동적 계획법(DP)** 개념을 기반으로 동작한다.  
모든 간선을 최대 `V - 1`번 반복하면서 최단 거리를 점진적으로 갱신한다.

![벨만-포드 동작 이미지 1](/assets/graph_algo/bellman_ford/image1.png)

1 - 3

![벨만-포드 동작 이미지 2](/assets/graph_algo/bellman_ford/image2.png)

![벨만-포드 동작 이미지 3](/assets/graph_algo/bellman_ford/image3.png)

![벨만-포드 동작 이미지 4](/assets/graph_algo/bellman_ford/image4.png)

### 동작 과정

1. 시작 정점의 거리를 0으로, 나머지 정점의 거리는 무한대로 초기화한다.
2. 전체 간선에 대해 `V - 1`번 반복하면서 다음을 수행한다:
    - `distance[u] + w < distance[v]`인 경우 `distance[v] = distance[u] + w`로 갱신
3. 마지막으로 한 번 더 모든 간선을 검사하여 갱신이 발생하면 **음의 사이클**이 존재하는 것이다.

---

## 3. 구현 방법

### Python 코드

```python
def bellman_ford(edges, V, start):
    # 1. 거리 초기화
    distance = [float('inf')] * V
    distance[start] = 0

    # 2. V-1번 모든 간선 확인
    for _ in range(V - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w

    # 3. 음의 사이클 확인
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[v] > distance[u] + w:
            raise ValueError("음의 사이클이 존재합니다.")

    return distance
```

## 4. 장단점 분석
### ✅ 장점
- 음의 가중치 허용
- 음의 사이클 탐지 가능
- 단순하고 직관적인 구현

### ❌ 단점
- 다익스트라보다 느림
- 간선 수가 많을수록 비효율적 (희소 그래프에 더 적합)

## 5. 시간복잡도 분석
| 연산 항목     | 시간복잡도     |
| --------- | --------- |
| 거리 갱신 반복  | O(V × E)  |
| 음의 사이클 확인 | O(E)      |
| 총 시간복잡도   | **O(VE)** |


- V: 정점 수
- E: 간선 수

## 6. 결론
벨만-포드는 음의 가중치 또는 음의 사이클 검출이 필요한 상황에서 매우 유용하다.
특히 금융 네트워크, 통신 네트워크 등에서 발생할 수 있는 비정상 루프 탐지에 효과적이다.

다익스트라가 음의 가중치에서 실패하는 반면, 벨만-포드는 안정적으로 결과를 낸다.

## 7. 참고
GeeksforGeeks - Bellman-Ford Algorithm
Wikipedia - Bellman–Ford algorithm