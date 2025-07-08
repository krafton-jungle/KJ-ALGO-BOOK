# 분할 정복 알고리즘 (Divide and Conquer Algorithm)

이 장에서는 분할 정복 알고리즘의 개념, 동작 방식, 구현 방법, 그리고 대표 적용 예제를 중심으로 학습한다.

> 분할 정복 알고리즘의 구조(Divide, Conquer, Merge)를 이해하고, 대표 알고리즘 예시를 통해 구현 방법과 시간 복잡도를 학습한다. 하위 문제의 독립성과 재귀적 처리 방식에 대한 이해를 바탕으로, 문제를 효율적으로 해결하는 전략을 배운다.

## 목차

| **항목** | **설명** |
| --- | --- |
| 핵심 키워드 정리 | 분할 정복 알고리즘의 정의, 주요 구조(Divide, Conquer, Merge), 시간복잡도, 공간복잡도 |
| 관련 개념 | 알고리즘의 기본 개념 이해를 위한 요소 (재귀, 하위 문제 독립성, 병렬성, 캐시 활용 등) |
| 알고리즘 실행 과정 | Merge Sort를 예시로 한 단계별 처리 과정을 시각적으로 표현한다 |
| 구현 예시 (Python) | Python으로 작성한 병합 정렬(Merge Sort) 예시 코드를 소개한다 |
| 참고 | 외부 사이트 및 문헌 출처 링크를 정리한다 |

## 핵심 키워드 정리

> 이 장에서 다루는 개념을 요약한다

- **정의**: 분할 정복(Divide and Conquer)은 문제를 더 작은 하위 문제로 나누고, 이를 각각 해결한 뒤 결과를 합쳐 전체 문제를 해결하는 알고리즘 설계 기법이다. 하위 문제들이 서로 독립적일 경우 병렬 처리나 성능 최적화에 유리하지만, 이는 분할 정복의 필수 조건은 아니다.
- **자료구조**: 배열, 리스트, 트리 등 (문제 유형에 따라 달라질 수 있다)
- **시간복잡도 (Merge Sort)**: O(N log N)
- **공간복잡도 (Merge Sort)**: O(N) – 병합 과정에서 임시 배열이 필요하여 추가 공간을 사용한다. <br>
일부 최적화된 구현에서는 공간복잡도를 줄일 수 있으나, 대부분의 구현은 O(N)의 추가 공간이 필요하다.
- **동작 방식 요약**:
  - 입력: 정렬되지 않은 배열
  - 처리: 배열을 절반으로 나누고 재귀적으로 정렬 및 병합한다
  - 출력: 정렬된 배열을 반환한다

## 관련 개념 (분할 정복을 이해하기 위한 기초)

> 분할 정복의 원리를 이해하기 위한 이론적 배경을 설명한다

- **재귀 (Recursion)**  
  → 함수가 자기 자신을 호출하는 방식이며, 분할 정복에서는 하위 문제를 재귀적으로 해결하는 데 사용된다.

- **하위 문제의 독립성**  
  → 각 하위 문제는 다른 하위 문제와 독립적으로 해결할 수 있어야 하며, 이에 따라 병렬 처리 또는 캐시 최적화에 유리하다.

- **병렬성 (Parallelism)**  
  → 하위 문제가 독립적인 경우, 병렬 처리가 가능하여 성능상의 이점을 얻을 수 있다. 그러나 모든 분할 정복 알고리즘이 병렬 처리에 적합한 것은 아니며, 예를 들어 Quick Sort는 분할 비대칭 시 병렬 효율이 낮을 수 있다.

- **Cache-Oblivious Algorithm**  
  → 작은 하위 문제들이 메모리 계층(예: 캐시)에 잘 맞도록 처리되는 구조로 되어 있어, 메모리 접근 효율이 높아진다.

## 알고리즘 실행 과정 (Merge Sort)

> Merge Sort 예제를 통해 단계별 구조를 시각적으로 설명한다

![분할 정복 흐름도](assets/recursion_algo/divide_and_conquer/divide_conquer_flow.png)

분할 정복 알고리즘은 다음과 같은 과정을 통해 문제를 해결한다.

1. 문제를 **작은 부분 문제**들로 나눈다.
2. 각 하위 문제를 **독립적으로 정복(해결)**한다.
3. 그 결과들을 **병합**하여 전체 문제의 해답을 완성한다.

- **파란색** 화살표: 문제를 작게 쪼개는 **분할(Divide)** 단계  
- **초록색** 화살표: 각 하위 문제를 해결하는 **정복(Conquer)** 단계  
- **노란색** 화살표: 하위 해답들을 결합하는 **병합(Merge)** 단계

> 이 구조는 Merge Sort, Quick Sort, Binary Search 등 다양한 알고리즘에서 사용된다.

## 구현 예시 (Python)

> 핵심 구조를 코드로 직접 확인한다

```python
# 병합 정렬 (Merge Sort) - Divide and Conquer 방식

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 배열을 절반으로 분할
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 분할된 결과를 병합
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # 두 배열을 정렬하며 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 사용 예시
arr = [5, 2, 4, 7, 1, 3, 6, 8]
sorted_arr = merge_sort(arr)

print(sorted_arr)  # 출력: [1, 2, 3, 4, 5, 6, 7, 8]
```

- **재귀 함수 구조**: `merge_sort()`는 배열을 반으로 나눈 뒤 각각 정렬하고 병합한다.  
- **핵심 병합 로직**: `merge()` 함수는 두 개의 정렬된 배열을 하나로 정렬하며 합친다.  
- **시간복잡도**: O(n log n)  
- **공간복잡도**: O(n) — 새로운 배열을 생성하여 결과를 저장한다

> 분할 정복은 단순한 문제 해결 기법을 넘어서, 복잡한 문제를 체계적으로 풀 수 있는 **핵심 설계 패턴**이다.  
> 다양한 문제를 접할 때, 문제를 나누고 정복하고 병합하는 관점에서 접근해 보자.

## 참고

- [GeeksforGeeks - Divide and Conquer](https://www.geeksforgeeks.org/divide-and-conquer-algorithm/)
- [Wikipedia - Divide and Conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- [Visualgo - Sorting Algorithms Visualization](https://visualgo.net/en/sorting)
