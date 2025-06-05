# 해시 테이블(Hash Table) vs. 트라이(Trie)
> **사전(dictionary)형 자료구조**라는 공통점을 갖지만,
> 키를 *어떻게* 저장‧검색하느냐에 따라 성격과 쓰임새가 달라진다. 두 자료구조를 함께 놓고 차이점과 공통점을 비교해보고자 한다.

---

## 공통점
- **목적**: 키 → 값(또는 존재 여부) 매핑을 빠르게 처리
- **주요 연산**: `삽입(insert)`, `탐색(search)`, `삭제(delete)`
- **성능 목표**: 대량 데이터에서도 *평균* `O(1)`(해시) 또는 `O(L)`(트라이) 수준 (*L은 데이터의 길이)
- **메모리 ↔︎ 속도** 트레이드오프: 배열·포인터를 넉넉히 잡아 검색 시간을 줄임

---

## 핵심 차이 한눈에 보기

| 구분 | **Hash Table** | **Trie (Prefix Tree)** |
|------|---------------|------------------------|
| **키 저장 방식** | 전체 키를 해시함수로 한 번에 변환 → 버킷 인덱스 | 키를 문자·비트 단위로 분해 → 노드 경로가 곧 키 |
| **평균 시간 복잡도** | `O(1)` (충돌 적고 테이블 적정 크기일 때) | `O(L)` (키 길이 **L**에 선형, 변함 없음) |
| **최악 시간 복잡도** | `O(n)` (충돌 모두 한 버킷에 몰릴 때) | `O(L)` (항상 동일) |
| **메모리 사용** | 키·값 저장 + 빈 슬롯/체이닝 오버헤드 | 알파벳 크기 × 레벨 수 ⇒ *희소 데이터*엔 낭비 |
| **충돌** | 해시 충돌 발생 → 체이닝·개방 주소법 필요 | 경로가 고유 ⇒ 구조적 충돌 없음 |
| **정렬/사전식 순회** | 별도 정렬 필요 → 느림 | 트리 순회만으로 즉시 사전식 순서 확보 |
| **접두사 검색** | 지원 어려움 (키 전체 필요) | 노드 하나로 동일 접두사 키 집합 확보 (`startsWith`, 자동완성) |
| **리사이징** | 버킷 가득 차면 **재해싱**(전체 재배치) | 필요 시 노드 추가만 → 전체 이동 없음 |
| **캐시 지역성** | 해시값이 랜덤 위치 → 캐시 미스 가능 | 동일 접두사 노드가 인접 → 캐시 친화적(배열 구현 시) |

---

## 구조별 특징 · 장단점

### 해시 테이블
| | |
|---|---|
| **특징** | 단일 해시값으로 *주소를 바로 점프*<br>테이블 크기는 보통 2^k 로 설정, 인덱스는 `hash & (size-1)` |
| **장점** | 평균 `O(1)` 속도, 구현 간단, 라이브러리 풍부, 메모리 탄력적 |
| **단점** | 충돌 관리 코드 필요, 최악 `O(n)` 위험, 접두사/순차 탐색 부적합 |
| **대표 사용 예** | 일반 키-값 캐시, 데이터베이스 인덱스, 중복 체크 집합 |

### 트라이
| | |
|---|---|
| **특징** | 키를 **경로 자체**로 저장 → 각 노드에 `children` 맵과 (선택) `value` 필드 |
| **장점** | 접두사 탐색·자동완성·사전식 순회가 자연스럽고 빠름, 최악 시간 `O(L)` 보장 |
| **단점** | 알파벳이 크거나 키가 드물면 메모리 낭비, 구현 복잡도 ↑ |
| **대표 사용 예** | 검색엔진 자동완성, 사전·단어 필터, IP·URL 라우팅, longest-prefix 매칭 |

## 해시 테이블 구현 코드

```python
class HashTable:
#버킷 배열: 실제 데이터를 저장하는 리스트들 (self.buckets)

# 충돌 처리 방식: Separate Chaining
# 하나의 인덱스에 여러 개 (key, value) 튜플을 리스트로 보관

#리사이징 조건: 버킷 사용률이 load_factor 초과하면 재해싱(rehash)

    def __init__(self, capacity: int = 8, load_factor: float = 0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # 해시 함수
    # 파이썬 내장 hash()는 음수도 나올 수 있어 & 0x7FFFFFFF로 양수 정규화
    # 인덱스 계산 시 mod capacity로 버킷 위치를 지정
    def _hash(self, key):
        return hash(key) & 0x7FFFFFFF

    # ⑥ 리사이징 (_rehash)
    # 테이블이 가득 찼을 때 버킷 수를 2배로 늘림
    # 모든 데이터를 다시 해시해서 재삽입
    def _rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self[k] = v

    # 삽입
    def __setitem__(self, key, value):
        if self.size / self.capacity > self.load_factor:
            self._rehash()
        # 모드 사용해서 인덱스 구하기
        idx = self._hash(key) % self.capacity
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    # 검색
    # 해시로 위치를 찾은 뒤 선형 탐색으로 키를 확인 (같은 버킷에 여러 키가 있을 수 있으므로)
    def __getitem__(self, key):
        idx = self._hash(key) % self.capacity
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    # 삭제 (__delitem__)
    # 해당 버킷에서 키를 찾아 제거
    # 리스트이므로 삭제는 O(n), 작은 해시테이블에선 실용적
    def __delitem__(self, key):
        idx = self._hash(key) % self.capacity
        bucket = self.buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return
        raise KeyError(key)


    # ⑤ 멤버 확인 (__contains__)
    def __contains__(self, key):
        idx = self._hash(key) % self.capacity
        return any(k == key for k, _ in self.buckets[idx])

    def __repr__(self):
        items = [f"{k!r}: {v!r}" for bucket in self.buckets for k, v in bucket]
        return "{" + ", ".join(items) + "}"

```
## 토막 상식!
- 파이썬의 hash() 함수는 내부적으로 32비트 또는 64비트 정수를 반환한다.
- 이 값은 음수도 포함될 수 있다.
- 하지만 배열의 인덱스로 사용하기 위해서는 양수의 정수로 변환해야 한다.
```python


```


## 장점 요약
O(1) 평균 시간 복잡도

키 타입에 제한 없음 (파이썬 hashable 객체이면 OK)

구조가 직관적이고 구현이 간단

## 단점
해시 충돌이 많아지면 O(n)까지 떨어질 수 있음

리스트 기반 체이닝이라 캐시 지역성은 낮음

리사이징 시 전체 해시 재계산 비용이 큼
## 트라이 구현 코드

```python
class TrieNode:
    __slots__ = ("children", "value")

    def __init__(self):
        self.children = {}
        self.value = None  # 값이 있으면 단어 끝

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, value=None):
        node = self.root
        for ch in key:
            node = node.children.setdefault(ch, TrieNode())
        node.value = value if value is not None else True

    def search(self, key: str):
        node = self.root
        for ch in key:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node.value

    def delete(self, key: str):
        def _delete(node, idx):
            if idx == len(key):
                if node.value is None:
                    return False
                node.value = None
                return len(node.children) == 0
            ch = key[idx]
            if ch not in node.children:
                return False
            should_prune = _delete(node.children[ch], idx + 1)
            if should_prune:
                del node.children[ch]
                return len(node.children) == 0 and node.value is None
            return False
        _delete(self.root, 0)

    def starts_with(self, prefix: str):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        words = []
        def dfs(nd, path):
            if nd.value is not None:
                words.append("".join(path))
            for c, child in nd.children.items():
                dfs(child, path + [c])
        dfs(node, list(prefix))
        return words

    def __repr__(self):
        return f"Trie(keys={self.starts_with('')})"

```

## 시간·공간 복잡도 요약

| 자료구조 | 삽입 | 탐색 | 삭제 | 메모리 (대략) |
|-----------|------|------|------|----------------|
| Hash Table | 평균 `O(1)`<br>최악 `O(n)` | 평균 `O(1)`<br>최악 `O(n)` | 평균 `O(1)`<br>최악 `O(n)` | `키+값` + `버킷` + 충돌체인 |
| Trie | `O(L)` | `O(L)` | `O(L)` | `Σ(알파벳^레벨)`<br>(희소 시 낭비) |

---