# 퀵정렬(Quick Sort)

이 장에서는 퀵정렬 알고리즘의 개념, 구현 방법, 그리고 실제 적용 예제를 중심으로 학습한다.
분할 정복 기법을 사용하여 피벗을 기준으로 배열을 재귀적으로 정렬하는 효율적인 알고리즘을 학습할 수 있다.

## 목차

| 항목 | 설명 |
|------|------|
| 핵심 키워드 정리 | 퀵정렬을 이해하는데 필요한 개념 |
| 퀵정렬이란 | 분할 정복과 피벗을 활용한 정렬 알고리즘 |
| 알고리즘 실행 과정 | 피벗 선택과 분할 과정을 시각화 |
| 구현 예시 (Python) | 파이썬으로 구현한 퀵정렬 예시 코드 |
| 참고 | 자료 출처 및 더 찾아보기 |

퀵정렬의 핵심인 분할 정복과 피벗 개념을 단계별로 이해할 수 있도록 구성하였다.

## 핵심 키워드 정리

* **정의**: 분할 정복 기법을 사용하여 피벗을 기준으로 배열을 재귀적으로 정렬하는 알고리즘이다.
* **자료구조**: 배열 (Array)
* **시간복잡도**: 평균 `O(n log n)`, 최악 `O(n²)`
* **공간복잡도**: `O(log n)` ~ `O(n)` (재귀 스택)
* **동작 방식 요약**:
  * **입력**: 정렬되지 않은 배열
  * **처리**: 피벗 선택 → 분할 → 재귀 정렬
  * **출력**: 정렬된 배열

## 퀵정렬이란

* 퀵정렬은 **토니 호어(Tony Hoare)**가 1960년에 개발한 정렬 알고리즘이다.
* **분할 정복(Divide and Conquer)** 전략을 사용한다.
* **피벗(Pivot)**을 기준으로 배열을 두 부분으로 나누어 정렬한다.
* **불안정 정렬**이지만 **제자리 정렬**이 가능하여 메모리 효율적이다.
* 평균적으로 다른 O(n log n) 알고리즘보다 빠른 성능을 보인다.


## 알고리즘 실행 과정

### 초기 배열: [64, 34, 25, 12, 22, 11, 90]

**1단계: 피벗 선택 (중간 원소: 12)**
```
[64, 34, 25, |12|, 22, 11, 90]
              ↑
             피벗 (인덱스: 3)
```

**2단계: 파티션 수행**
```
피벗보다 작은 값들을 왼쪽으로, 큰 값들을 오른쪽으로 분할

작은 값들: [11]
피벗: [12]
큰 값들: [64, 34, 25, 22, 90]

결과: [11] + [12] + [64, 34, 25, 22, 90]
```

**3단계: 재귀적 정렬**
```
왼쪽 부분배열 [11]: 원소가 1개이므로 정렬 완료

오른쪽 부분배열 [64, 34, 25, 22, 90]을 피벗 25로 분할:
- 작은 값: [22]
- 피벗: [25]  
- 큰 값: [64, 34, 90]

계속해서 재귀적으로 정렬...

최종 결과: [11, 12, 22, 25, 34, 64, 90]
```

### 재귀 호출 트리
```
quick_sort([64, 34, 25, 12, 22, 11, 90])
│                    ↓ 피벗: 12
├── quick_sort([11])                       ← 12보다 작은 값들 (정렬 완료)
└── quick_sort([64, 34, 25, 22, 90])       ← 12보다 큰 값들
                     ↓ 피벗: 25
    ├── quick_sort([22])                   ← 25보다 작은 값들 (정렬 완료)
    └── quick_sort([64, 34, 90])           ← 25보다 큰 값들
                     ↓ 피벗: 34
        ├── quick_sort([])                 ← 34보다 작은 값들 (없음)
        └── quick_sort([64, 90])           ← 34보다 큰 값들
                     ↓ 피벗: 90
            ├── quick_sort([64])           ← 90보다 작은 값들 (정렬 완료)
            └── quick_sort([])             ← 90보다 큰 값들 (없음)
```

## 구현 예시 (Python)

### 기본 퀵정렬 구현

```python
def quick_sort(arr):
    """
    가장 기본적인 퀵정렬 구현
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 중간 원소를 피벗으로 선택
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# 사용 예시
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"원본: {arr}")
sorted_arr = quick_sort(arr)
print(f"정렬: {sorted_arr}")
```

### 제자리 정렬 구현 (Lomuto 파티션)

```python
def lomuto_partition(arr, low, high):
    """
    Lomuto 파티션: 마지막 원소를 피벗으로 사용
    """
    pivot = arr[high]  # 마지막 원소를 피벗으로 선택
    i = low - 1        # 작은 원소들의 인덱스
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 피벗을 올바른 위치에 배치
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_inplace(arr, low=0, high=None):
    """
    제자리 퀵정렬
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 파티션 수행
        pivot_index = lomuto_partition(arr, low, high)
        
        # 재귀 호출
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

# 사용 예시
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"원본: {arr}")
quick_sort_inplace(arr)
print(f"정렬: {arr}")
```

### 랜덤 피벗 퀵정렬

```python
import random

def random_partition(arr, low, high):
    """
    랜덤 피벗을 사용한 파티션
    """
    # 랜덤 인덱스 선택 후 마지막과 교환
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    
    return lomuto_partition(arr, low, high)

def quick_sort_random(arr, low=0, high=None):
    """
    랜덤 피벗을 사용한 퀵정렬 (최악의 경우 방지)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = random_partition(arr, low, high)
        quick_sort_random(arr, low, pivot_index - 1)
        quick_sort_random(arr, pivot_index + 1, high)

# 사용 예시
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"원본: {arr}")
quick_sort_random(arr)
print(f"정렬: {arr}")
```

## 참고

### 참고한 자료
* **『Introduction to Algorithms』** - Thomas H. Cormen
  * Chapter 7: Quicksort
* **『Algorithms』** - Robert Sedgewick, Kevin Wayne  
  * Chapter 2.3: Quicksort

### 추가로 참고하면 좋은 자료
* **온라인 시각화 도구**
  * [VisuAlgo - Quick Sort](https://visualgo.net/en/sorting)
* **문제 해결 사이트**
  * [GeeksforGeeks - Quick Sort](https://www.geeksforgeeks.org/quick-sort/)