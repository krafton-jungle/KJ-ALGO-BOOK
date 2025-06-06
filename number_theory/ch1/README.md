# 정수론 (Number Theory)

## 1. 정수론이란?

정수론은 수학의 한 분야로, **정수**를 중심으로 수의 구조, 소수, 최대공약수, 최소공배수, 모듈러 연산 등 **수의 본질적인 성질**을 탐구하는 학문이다.
정수론은 암호학, 알고리즘, 컴퓨터 과학 등 다양한 분야와 깊은 관련이 있다.

그 전에 자주 쓰는 수학기호는 [여길](https://namu.wiki/w/%EC%88%98%ED%95%99/%EC%95%BD%EC%96%B4%20%EB%B0%8F%20%EA%B8%B0%ED%98%B8) 참고하길 바란다.

---

## 2. 정수의 연산 및 특징

먼저 우리는 다음과 같은 개념을 알아야 한다.

### 1. 연산이 닫혀 있다 (Closed)

정수 집합 {% math %}\mathbb{Z}{% endmath %}에 대해, 어떤 연산 {% math %}\mathbin{\circledast}{% endmath %}가 다음 조건을 만족하면 **닫혀 있다**고 한다.

$$
\forall a, b \in \mathbb{Z},\ a \mathbin{\circledast} b \in \mathbb{Z}
$$

모든 정수 a,b에 대해 어떤 연산을 해도 정수가 나올 때 그 연산은 닫혀 있다고 한다.

예를 들어, 덧셈 {% math %}(+){% endmath %}, 뺄셈 {% math %}(-){% endmath %}, 곱셈 {% math %}(\times){% endmath %}은 {% math %}\mathbb{Z}{% endmath %}에서 닫혀 있다:

$$
\{ a \mathbin{\circledast} b\ |\ a, b \in \mathbb{Z} \} \subseteq \mathbb{Z} \quad \text{where } \mathbin{\circledast} \in \{+, -, \times\}
$$

---

### 2. 연산이 열려 있다 (Not Closed/Open)

$$
\exists a, b \in \mathbb{Z},\ b \ne 0,\ \frac{a}{b} \notin \mathbb{Z}
$$

어떤 연산이 집합 내 원소들의 계산 결과를 항상 같은 집합에 포함시키지 않는다면, **열려 있다**고 한다.

예를 들어, 나눗셈 {% math %}(\div){% endmath %}은 정수 집합 {% math %}\mathbb{Z}{% endmath %}에서 닫혀 있지 않다:

$$
1, 2 \in \mathbb{Z} \quad \text{but} \quad \frac{1}{2} \notin \mathbb{Z}
$$

예시: 1과 2는 정수지만 {% math %}\frac{1}{2}{% endmath %}는 정수가 아니다.

따라서, 정수의 나눗셈 연산은 닫혀 있지 않다:

$$
\left\{ \frac{a}{b}\ \middle|\ a, b \in \mathbb{Z},\ b \ne 0 \right\} \nsubseteq \mathbb{Z}
$$

---

### 3. 항등원 (Identity Element)

집합 {% math %}S{% endmath %}와 연산 {% math %}\mathbin{\circledast}{% endmath %}에 대해, 원소 {% math %}e \in S{% endmath %}가 다음 조건을 만족하면 **항등원**이라고 한다:

$$
\forall a \in S,\ a \mathbin{\circledast} e = e \mathbin{\circledast} a = a
$$

집합의 모든 원소와 연산했을 때 자기 자신이 나오는 원소를 항등원이라고 한다.

#### 덧셈의 항등원

정수 집합 {% math %}\mathbb{Z}{% endmath %}에서 덧셈 {% math %}(+){% endmath %}의 항등원은 {% math %}0{% endmath %}이다.

$$
\forall a \in \mathbb{Z},\ a + 0 = 0 + a = a
$$

예시: {% math %}5 + 0 = 0 + 5 = 5{% endmath %}</br> {% math %}(-3) + 0 = 0 + (-3) = -3{% endmath %}

#### 곱셈의 항등원

정수 집합 {% math %}\mathbb{Z}{% endmath %}에서 곱셈 {% math %}(\times){% endmath %}의 항등원은 {% math %}1{% endmath %}이다.

$$
\forall a \in \mathbb{Z},\ a \times 1 = 1 \times a = a
$$

예시: {% math %}7 \times 1 = 1 \times 7 = 7{% endmath %}<br>{% math %}(-4) \times 1 = 1 \times (-4) = -4{% endmath %}

---

### 4. 역원 (Inverse Element)

집합 {% math %}S{% endmath %}와 연산 {% math %}\mathbin{\circledast}{% endmath %}, 그리고 항등원 {% math %}e{% endmath %}가 주어졌을 때, 원소 {% math %}a \in S{% endmath %}에 대해 다음 조건을 만족하는 원소 {% math %}a^{-1} \in S{% endmath %}가 존재하면 {% math %}a^{-1}{% endmath %}을 {% math %}a{% endmath %}의 **역원**이라고 한다:

$$
a \mathbin{\circledast} a^{-1} = a^{-1} \mathbin{\circledast} a = e
$$

어떤 원소와 연산했을 때 항등원이 나오는 원소를 역원이라고 한다.

#### 덧셈의 역원 (음수)

정수 집합 {% math %}\mathbb{Z}{% endmath %}에서, 모든 정수 {% math %}a{% endmath %}에 대해 덧셈 역원 {% math %}(-a){% endmath %}가 존재한다:

$$
\forall a \in \mathbb{Z},\ a + (-a) = (-a) + a = 0
$$

예시:
- {% math %}5{% endmath %}의 덧셈 역원은 {% math %}-5{% endmath %}이다. 
- {% math %}5 + (-5) = (-5) + 5 = 0{% endmath %}
- {% math %}(-3){% endmath %}의 덧셈 역원은 {% math %}3{% endmath %}이다. 
- {% math %}(-3) + 3 = 3 + (-3) = 0{% endmath %}

#### 곱셈의 역원 (역수)

정수 집합 {% math %}\mathbb{Z}{% endmath %}에서는, {% math %}1{% endmath %}과 {% math %}-1{% endmath %}을 제외하고는 곱셈 역원이 존재하지 않는다:

$$
\forall a \in \mathbb{Z} - \{-1, 1\},\ \nexists a^{-1} \in \mathbb{Z}\;\;\text{s.t.}\;\;a \times a^{-1} = 1
$$


예시:
- {% math %}1{% endmath %}의 곱셈 역원은 {% math %}1{% endmath %}이다: {% math %}1 \times 1 = 1{% endmath %}
- {% math %}(-1){% endmath %}의 곱셈 역원은 {% math %}(-1){% endmath %}이다: {% math %}(-1) \times (-1) = 1{% endmath %}
- {% math %}2{% endmath %}의 곱셈 역원은 {% math %}\frac{1}{2}{% endmath %}이지만, {% math %}\frac{1}{2} \notin \mathbb{Z}{% endmath %}이므로 정수 집합에서는 곱셈 역원이 존재하지 않는다.

$$

\{a \in \mathbb{Z}\ |\ \exists a^{-1} \in \mathbb{Z}, a \times a^{-1} = 1\} = \{-1, 1\}
$$

---

## 3. 나눗셈 정리 (Division Algorithm)

나눗셈 정리는 정수론의 가장 기본적이고 중요한 정리 중 하나로, 모든 정수를 다른 정수로 나눈 결과를 명확하게 표현해준다.

### 나눗셈 정리

임의의 정수 {% math %}a{% endmath %}와 양의 정수 {% math %}b > 0{% endmath %}에 대해, 다음 조건을 만족하는 **유일한** 몫인 {% math %}q{% endmath %}와 나머지 {% math %}r{% endmath %}이 언제나 존재한다.

$$
a = bq + r, \quad 0 \leq r < b
$$

여기서
- {% math %}a{% endmath %}: **피제수** (dividend)
- {% math %}b{% endmath %}: **제수** (divisor)
- {% math %}q{% endmath %}: **몫** (quotient)
- {% math %}r{% endmath %}: **나머지** (remainder)

이다.

---

### 나눗셈 정리의 의미

이 정리는 어떤 정수든지 양의 정수로 나누면, 항상 **유일한 몫과 나머지**가 존재함을 보장한다. 특히 나머지는 항상 {% math %}0{% endmath %} 이상 제수 미만의 값을 가진다.

### 예시

#### 예시 1: 양수 나누기
{% math %}17{% endmath %}을 {% math %}5{% endmath %}로 나누는 경우:

$$
17 = 5 \times 3 + 2
$$

- 피제수: {% math %}a = 17{% endmath %}
- 제수: {% math %}b = 5{% endmath %}
- 몫: {% math %}q = 3{% endmath %}
- 나머지: {% math %}r = 2{% endmath %} ({% math %}0 \leq 2 < 5{% endmath %})

#### 예시 2: 음수 나누기
{% math %}(-23){% endmath %}을 {% math %}7{% endmath %}로 나누는 경우:

$$
-23 = 7 \times (-4) + 5
$$

- 피제수: {% math %}a = -23{% endmath %}
- 제수: {% math %}b = 7{% endmath %}
- 몫: {% math %}q = -4{% endmath %}
- 나머지: {% math %}r = 5{% endmath %} ({% math %}0 \leq 5 < 7{% endmath %})

**주의**: 나머지는 항상 {% math %}0{% endmath %} 이상이다. 즉 {% math %}(-23) = 7 \times (-3) + (-2){% endmath %}는 올바른 표현이 아니다.

#### 예시 3: 나누어떨어지는 경우
{% math %}21{% endmath %}을 {% math %}7{% endmath %}로 나누는 경우:

$$
21 = 7 \times 3 + 0
$$

- 몫: {% math %}q = 3{% endmath %}
- 나머지: {% math %}r = 0{% endmath %}

---

### 나눗셈 정리의 활용

#### 1. 나머지에 따른 정수 분류(잉여류)
임의의 정수는 어떤 양의 정수 {% math %}n{% endmath %}으로 나눈 나머지에 따라 {% math %}n{% endmath %}개의 집합으로 분류할 수 있다:

$$
\mathbb{Z} = \{nk : k \in \mathbb{Z}\} \cup \{nk + 1 : k \in \mathbb{Z}\} \cup \cdots \cup \{nk + (n-1) : k \in \mathbb{Z}\}
$$

예를 들어, 모든 정수는 3으로 나눈 나머지에 따라 다음과 같이 분류된다:
- {% math %}3k{% endmath %} 형태: ..., -6, -3, 0, 3, 6, 9, ...
- {% math %}3k + 1{% endmath %} 형태: ..., -5, -2, 1, 4, 7, 10, ...
- {% math %}3k + 2{% endmath %} 형태: ..., -4, -1, 2, 5, 8, 11, ...

#### 2. 홀수와 짝수
모든 정수는 2로 나눈 나머지에 따라 분류된다:

$$
\text{짝수}: a = 2k \quad (k \in \mathbb{Z})
$$

$$
\text{홀수}: a = 2k + 1 \quad (k \in \mathbb{Z})
$$

---

### 나눗셈 정리의 존재성과 유일성

#### 존재성
어떤 정수 {% math %}a{% endmath %}와 양의 정수 {% math %}b{% endmath %}에 대해, 조건을 만족하는 {% math %}q{% endmath %}와 {% math %}r{% endmath %}이 **반드시 존재**한다.

**증명 (귀류법)**

{% math %}S = \{a - bk : k \in \mathbb{Z}, a - bk \geq 0\}{% endmath %}라고 하자.

즉 {% math %}S{% endmath %}는 {% math %}a - bk{% endmath %}가 0 이상인 정수 {% math %}k{% endmath %}에 대해 그 값을 모은 집합이다.

{% math %}S{% endmath %}가 {% math %}\emptyset{% endmath %}(공집합)이라고 가정하자. 그러면 모든 정수 {% math %}k{% endmath %}에 대해 {% math %}a - bk < 0{% endmath %}이다. 즉, {% math %}a < bk{% endmath %}이다.

{% math %}k{% endmath %}를 충분히 작게 (음수로) 선택하면 {% math %}bk{% endmath %}는 {% math %}a{% endmath %}보다 작아질 수 있다. 특히 {% math %}k = \lfloor \frac{a}{b} \rfloor - 1{% endmath %}로 선택하면 {% math %}bk < a{% endmath %}가 되어 모순이다.

따라서 {% math %}S{% endmath %}는 {% math %}\emptyset{% endmath %}이 아니고, {% math %}S{% endmath %}는 음이 아닌 정수들의 집합이므로 최솟값 {% math %}r{% endmath %}이 존재한다. 이때 {% math %}r = a - bq{% endmath %}인 정수 {% math %}q{% endmath %}가 존재한다.

{% math %}r \geq b{% endmath %}라고 가정하자. 그러면 {% math %}r - b = a - bq - b = a - b(q+1) \geq 0{% endmath %}이고, {% math %}r - b < r{% endmath %}이므로 {% math %}r{% endmath %}이 최솟값이라는 것에 모순이다.

따라서 {% math %}0 \leq r < b{% endmath %}이고, {% math %}a = bq + r{% endmath %}인 {% math %}q, r{% endmath %}이 존재한다.

#### 유일성
조건을 만족하는 {% math %}q{% endmath %}와 {% math %}r{% endmath %}은 **유일**하다.

**증명 (귀류법)**

{% math %}a = bq_1 + r_1 = bq_2 + r_2{% endmath %}이고 {% math %}0 \leq r_1, r_2 < b{% endmath %}를 만족하는 서로 다른 두 쌍 {% math %}(q_1, r_1){% endmath %}과 {% math %}(q_2, r_2){% endmath %}가 존재한다고 가정하자.

{% math %}q_1 \neq q_2{% endmath %}라고 가정하자. {% math %}q_1 > q_2{% endmath %}라고 하면:

$$
bq_1 + r_1 = bq_2 + r_2
$$

$$
b(q_1 - q_2) = r_2 - r_1
$$

{% math %}q_1 > q_2{% endmath %}이므로 {% math %}q_1 - q_2 \geq 1{% endmath %}이다. 따라서:

$$
b(q_1 - q_2) \geq b \cdot 1 = b
$$

한편, {% math %}0 \leq r_1, r_2 < b{% endmath %}이므로:

$$
r_2 - r_1 < b - 0 = b
$$

$$ 
r_2 - r_1 > 0 - b = -b
$$

즉, {% math %}|r_2 - r_1| < b{% endmath %}이다.

그런데 {% math %}b(q_1 - q_2) = r_2 - r_1{% endmath %}이고 {% math %}b(q_1 - q_2) \geq b{% endmath %}이면서 {% math %}|r_2 - r_1| < b{% endmath %}이므로 모순이다.

따라서 {% math %}q_1 = q_2{% endmath %}이고, 이로부터 {% math %}r_1 = r_2{% endmath %}이다.

### 확장된 나눗셈 정리

나누는 수(제수)가 음수인 경우에도 나눗셈 정리를 확장할 수 있다. 정수 {% math %}a{% endmath %}와 {% math %}b \neq 0{% endmath %}에 대해:

$$
a = bq + r, \quad 0 \leq r < |b|
$$

예시: {% math %}17{% endmath %}을 {% math %}(-5){% endmath %}로 나누는 경우:

$$
17 = (-5) \times (-3) + 2
$$

여기서 {% math %}0 \leq 2 < |-5| = 5{% endmath %}이다.

---

## 약수와 배수

#### 약수 (Divisor)
- 정수 {% math %}a{% endmath %}와 {% math %}b{% endmath %}에 대해, {% math %}a = bk{% endmath %}인 어떤 정수 {% math %}k{% endmath %}가 존재하면,
- {% math %}b{% endmath %}를 {% math %}a{% endmath %}의 약수(또는 인수, divisor, factor)라고 하고,
- {% math %}a{% endmath %}를 {% math %}b{% endmath %}의 배수(multiple)라고 한다.

예시:

- {% math %}12 = 3 \times 4{% endmath %}이므로, 3과 4는 12의 약수이다.

- {% math %}15 = (-5) \times (-3){% endmath %}이므로, -5와 -3도 15의 약수이다.

- 어떤 정수도 자기 자신과 1(또는 -1)의 배수이므로, 모든 정수는 자기 자신과 ±1의 약수를 가진다.

#### 배수 (Multiple)
정수 {% math %}a{% endmath %}에 대해, 어떤 정수 {% math %}k{% endmath %}에 대해 {% math %}a = bk{% endmath %}로 표현될 수 있으면,
{% math %}a{% endmath %}는 {% math %}b{% endmath %}의 배수이다.

예시:

- 20은 4의 배수이다. ({% math %}20 = 4 \times 5{% endmath %})

- 15는 3의 배수이다. ({% math %}-15 = 3 \times (-5){% endmath %})

성질 요약
- {% math %}b \mid a{% endmath %}라고 쓰면, “{% math %}b{% endmath %}가 {% math %}a{% endmath %}를 나눈다” 혹은 “{% math %}b{% endmath %}는 {% math %}a{% endmath %}의 약수이다”를 의미한다.

- {% math %}b \nmid a{% endmath %}는 나누어떨어지지 않음을 의미한다.

- {% math %}0{% endmath %}은 모든 정수의 배수이다. ({% math %}a \mid 0{% endmath %}는 항상 참)

- {% math %}0{% endmath %}은 어떤 수의 약수도 아니다. (단, {% math %}0 \mid a{% endmath %}는 a가 0일 때만 성립)