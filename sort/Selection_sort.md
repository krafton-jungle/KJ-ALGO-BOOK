# 선택 정렬(Selection Sort)
## 선택정렬이란
선택 정렬은 가장 작은(또는 가장 큰) 원소를 찾아 순서대로 정렬하는 기초적인 정렬 알고리즘이다. 구현이 간단하고 직관적이어서 기본 개념을 익히는 데 적합하지만, 시간 복잡도가 $O(N^2)$로 비효율적이기 때문에 데이터 양이 적은 경우를 제외하면 실무에서는 거의 사용되지 않는다.

![선택 정렬 과정](/assets/sort/selection_sort_animation.gif)
## 정렬 과정 (오름차순 기준)
1. 최솟값 찾기: 정렬되지 않은 부분의 배열에서 가장 작은 값을 찾는다.
2. 교체: 찾은 최솟값을 해당 부분의 첫 번째 원소와 교환한다.
3. 반복: 정렬되지 않은 부분이 없어질 때까지 위 과정을 반복한다.

### 과정 예시
```
초기:  [29, 10, 14, 37, 11]
1회전: [10, 29, 14, 37, 11]
2회전: [10, 11, 14, 37, 29]
3회전: [10, 11, 14, 37, 29]
4회전: [10, 11, 14, 29, 37]
최종:  [10, 11, 14, 29, 37]
```

## 특징
- 시간 복잡도는 $O(N^2)$이다. 항상 같은 횟수만큼 비교하기 때문에 최선, 평균, 최악의 경우 모두 동일한 시간 복잡도를 가진다.
- 공간 복잡도는 $O(1)$이다. 주어진 배열 안에서 이루어지는 제자리 정렬(in-place)로 추가적인 메모리가 거의 필요 없다.
- 불안정 정렬(Unstable Sort)이라 같은 값을 가지는 항목들의 순서가 정렬 과정에서 바뀔 수 있다.

## 구현 예시 (Python)
``` python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # 현재 위치를 최소값 인덱스로 가정
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # 더 작은 값이 있으면 위치 갱신
        arr[i], arr[min_index] = arr[min_index], arr[i]  # 스왑
```

## 이중 선택 정렬
- 이중 선택 정렬은 한 번의 탐색에서 최솟값과 최댓값을 동시에 선택해서 양쪽 끝에 각각 배치하는 방식이다.
- 반복 횟수는 줄어들지만, 한 회차에 최솟값과 최댓값을 모두 탐색하므로 비교 횟수는 여전히 많으며 최악 시간 복잡도는 $O(N^2)$이다.

### 구현 예시 (Python)
```python
def double_selection_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # 최소, 최대 인덱스 초기화
        min_index = left
        max_index = left

        for i in range(left, right + 1):
            if arr[i] < arr[min_index]:
                min_index = i
            if arr[i] > arr[max_index]:
                max_index = i

        # 최솟값을 왼쪽으로 이동
        arr[left], arr[min_index] = arr[min_index], arr[left]

        # 만약 max_index가 left였다면, min_index와 바뀌어서 max_index를 갱신
        if max_index == left:
            max_index = min_index

        # 최댓값을 오른쪽으로 이동
        arr[right], arr[max_index] = arr[max_index], arr[right]

        left += 1
        right -= 1
```

## 참고
- 참고한 자료
    - [위키백과 - 선택 정렬](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%A0%95%EB%A0%AC)
- 이미지 출처
    - 2차 출처: [velog - velgmzz.log](https://velog.io/@velgmzz/Algorithm-%EC%84%A0%ED%83%9D-%EC%A0%95%EB%A0%AC-Selection-Sort)
    - 원 출처: [Visualgo](https://visualgo.net)
- 추가로 참고하면 좋은 자료
    - [Visualgo - Sorting Algorithms](https://visualgo.net/en/sorting)