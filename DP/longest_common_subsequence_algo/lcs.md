## 핵심 개념

### LCS란?
두 수열에서 순서를 유지하면서 공통으로 나타나는 가장 긴 부분수열
### 예시
X = 'ABCDEFG'
Y = 'ARETEG'
일 경우 `AEG` 가 **최장공통부분수열** 이 된다.

> 공통부분 문자열과 혼동을 조심한다

> 공통부분 문자열 Longest Common String은 문자열이 연속해야 한다.

## 알고리즘 동작 원리

1. DP 테이블 구성: `dp[i][j] = X[0:i]와 Y[0:j]의 LCS 길이`
2. 점화식:
```python
    LCS[i][j] = 
                0  (i=0 또는 j=0)
                LCS[i-1][j-1] + 1  (X[i] == Y[j])
                max(LCS[i-1][j], LCS[i][j-1]) (X[i] != Y[j])
```

3. **복잡도**:
    - 시간: O(m × n)
    - 공간: O(m × n) 또는 O(min(m,n))
### 그림설명
#### 재귀적 접근
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fc45P37%2FbtsPFjvJbNZ%2FAAAAAAAAAAAAAAAAAAAAAIQxzAKQgGp4pz-sCs1V26_PjHaWqZoc8dQAc8u73drz%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1756652399%26allow_ip%3D%26allow_referer%3D%26signature%3DtcW8RBAHTlG7J0%252FOerJlSZbYQLw%253D">

**마지막 문자를 비교 후 문자열을 줄여가며 값을 생성하는 방식**
1. 이 케이스에선 마지막 부분이 같으니 하나씩 제거한 후 다시 비교
```
X = ABC'D'
Y = BEF'D'
```
2. 이 케이스에선 다르니 하나씩 제거한 문자열을 비교
```
X = AB'C'
Y = BE'F'
```
2-1.
```
X = A'B
Y = BE'F
```
2-2.
```
X = AB'C'
Y = B'E'
```
이런 과정으로 문자열이 없어질때까지 반복 후 재귀적으로 기존문제를 해결

## 알고리즘 구현 과정
### 상향식 접근
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FIneJ9%2FbtsPEpDo4dl%2FAAAAAAAAAAAAAAAAAAAAAHdUlkgU-h-0u1LmrCG5dYBg0va_OrRkALe-JTjtY8rx%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1756652399%26allow_ip%3D%26allow_referer%3D%26signature%3DxVoNkvMgtmWpOQlb49m%252Brla61BY%253D">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2Fcftz6U%2FbtsPFjvJbPK%2FAAAAAAAAAAAAAAAAAAAAANUaEL72L0OU5dYyUUC13CUFlggS8dR0gsMbsvbwOGii%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1756652399%26allow_ip%3D%26allow_referer%3D%26signature%3DL2gkLymRXxuvPZsZTqQGBUQnypM%253D">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FNKhjB%2FbtsPD1bpsQR%2FAAAAAAAAAAAAAAAAAAAAAAHnNuGkE4oqYd_w16dkUnYoQcbvSEbZo9ZdkiJYu_Om%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1756652399%26allow_ip%3D%26allow_referer%3D%26signature%3Dt5LSzaUzUvS2bouZRGsC2SVbRz0%253D">


## 코드구현 (Python)
### 탑다운방식
- 복잡도 O(2^n)
```python
def lcs(x, y):
	m, n = len(x), len(y)
	if m == 0 or n == 0: # 문자열이 하나도 없을 시 탈출
		return 0
	else:
		if x[-1] == y[-1]: # 마지막 문자열이 같다면
			return lcs(x[: (m-1)], y[: (n-1) ]) +1
		else: 
			return max(lcs(x[: (m-1)], y[:n]) , lcs(x[:m], y[:(n-1)]))
```

### 탑다운방식 + 메모이제이션
- 복잡도 O(mn)
```python
def lcs_topdown_with_dp(x, y, memo=None):
    """메모화 버전"""
    if memo is None:
        memo = {}

    m, n = len(x), len(y)

    # 이미 계산된 결과가 있으면 반환
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0: # 탈출조건
        result = 0
    else:
        if x[-1] == y[-1]:
            result = lcs_topdown_with_dp(x[: (m - 1)], y[: (n - 1)], memo) + 1
        else:
            result = max(
                lcs_topdown_with_dp(x[: (m - 1)], y, memo),
                lcs_topdown_with_dp(x, y[: (n - 1)], memo),
            )

    memo[(m, n)] = result
    return result
```

### 상향식접근 dp
- 복잡도 O(mn)
```python
def lcs_bottomup(x, y):
    x, y = [""] + x, [""] + y  # 인덱스 통일
    m, n = len(x), len(y)

    dp = [[0 for _ in range(n)] for _ in range(m)] 
    # 최대값을 저장할 리스트
    b = [[0 for _ in range(n)] for _ in range(m)]  
    # 참고위치를 저장할 리스트
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                b[i][j] = 1 # 대각선을 참고했으면 1을 저장
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                b[i][j] = 2 if dp[i - 1][j] > dp[i][j - 1] else 3 
                # Y의 문자열을 참고했으면 2, X의 문자열을 참고했으면 3
    return c, b
```

## 출처
[주니온TV 아무거나 연구소](https://www.youtube.com/watch?v=z8KVLz9BFIo&t=14s)

[emplam27_velog](https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence)

## 연습문제
[백준 9251 LCS](https://www.acmicpc.net/problem/9251)

[백준 9252 LCS2](https://www.acmicpc.net/problem/9252)