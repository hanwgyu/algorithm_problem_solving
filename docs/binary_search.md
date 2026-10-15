# Binary Search

## 구현 방식
아래와 같이 두가지 방식으로 구현할 수 있다.
```py
l, r = 0, len(a)     # 핵심: r = n
while l < r:
    m = (l + r) // 2
    if a[m] < x:
        l = m + 1
    else:
        r = m
return l
```

또는

```py
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    m = 0

    while low <= high:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            return m
    return -1
```
2번 구현 방식을 쓰자.  외우기도 쉽고, arr 크기가 1일때도 사용할 수 있다. (아래에서 설명)


## 1번 vs 2번

```
mid를 버리면 안 되는 문제 → while l < r
mid를 버릴 수 있는 문제 → while l <= r
```

1번은  “경계 찾기” 문제에 사용된다. 왼쪽이나 오른쪽을 버리지 않기 때문에, 명확한 경계를 찾는데 사용된다.
	•	peak 찾기
	•	lower/upper bound
	•	“정답이 index 하나로 수렴하는 문제”
ex) https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

```
while l < r:
    m = (l + r) // 2
    if cond(m):
        r = m
    else:
        l = m + 1
```

✅ 구간 의미
	•	후보는 [l, r) (오른쪽 끝 r은 “포함 안 함”)
	•	종료는 항상 l == r (정말 “수렴”)

✅ 각 스텝 의미
	•	a[m] < x → m 포함 왼쪽 전부 버려도 됨 → l = m+1
	•	else (a[m] >= x) → m 자체가 답일 수도 있으니 남김 → r = m

✅ 종료 상태
	•	항상 l == r
	•	그 값은 첫 >= x 위치 (lower_bound)
	•	“정확히 존재하는지”는 마지막에 a[l]==x로 확인d


2번은 기존 값찾기 문제.

### 정리. 
✅ 1. “값 찾기”면 무조건 l <= r
	•	standard binary search
	•	rotated array search
	•	조건 분기가 명확한 경우

✅ 2. “경계 찾기”면 l < r
	•	lower_bound
	•	peak
	•	최소 만족 index


✅ 3. 변형 문제는 이렇게 생각

```
mid를 보고
→ 왼쪽을 통째로 버릴 수 있는가?
→ 오른쪽을 통째로 버릴 수 있는가?
```

## 어려운점..

binary search를 바꿔서 쓰는 알고리즘은 매우 구현하기 어려울 수 있다.
[example](Leetcode/Search_in_Rotated_Sorted_Array.py) 꼭 확인해볼것.
조건에 따라 오른쪽으로 갈지 왼쪽으로 갈지, 모든 경우를 체크하지 않기에 어렵다. (jumping condition이 존재한다.)


#### 특히 , 원소개수가 2개일때 (ex) find 3 in [1,3])

위의 2번 솔루션에서 l ==m==0이 되기때문에 조건문이  r= m-1로 진행될경우  그다음에 바로 while문을 빠져나온다. 근데 이러면 1인 부분을 체크할 수 없다.
l=m+1이 되면, 1인 idx도 체크해서 괜찮긴하다.

r=m-1일때 jumping condition 을 해결하려면, 조건문 내에서 l,r 까지 매번 같이 체크해줘야하는 수 밖에 없는듯..?
while문을 빠져나오고서는 l=0, r=-1이기 때문에 1인 idx를 체크할 수없다..

그러나 1번 솔루션에서는 r=m으로 조건문이 진행되면, 똑같이 안되는데. l=m+1 이 되어도 1인 idx를 체크할 수 없다.

#### 원소개수가 1개일때는

2번 솔루션은 문제가 없다.

1번 솔루션으로 풀면 while 문 자체를 들어가지 않는다.

**결론은 2번 솔루션이 낫고, 원소 개수가 2개일때 (binarysearch가 진행되서 2개로 줄어들었을때도) 예외 케이스들이 많아서 항상 구현시  경우의 수들을 생각해봐야한다.**



## 좋은 문제들

### 변형된 Binary search
Array에서 O(logN) 시간에 어떤 값을 찾아내는 문제. Binary Search의 조건을 변형해서 구현한다.

#### Example problems
- 33. Search in Rotated Sorted Array
- 162. Find Peak Element
- 4. Median of Two Sorted Arrays

## Binary Search as Answer
- 정답을 특정 값으로 추정하고, 정답의 범위를 Binary Search로 이동하면서 구하는 방식도 자주 쓰인다.
- 예시 문제: https://leetcode.com/problems/find-the-duplicate-number/

## 템플릿과 엣지 케이스
- Binary Search 문제는 Template이 두 가지가 있다. 템플릿에 따라 예외처리를 해줘야 하는 경우가 있고, 안 해도 모든 케이스가 고려되는 경우가 있다.
- 참고 문제: https://github.com/hanwgyu/algorithm_problem_solving/blob/master/Leetcode/162.py
- 엣지 케이스를 반드시 고려해서 결과를 l, r 중 뭘 리턴할지 고려해야 하고, 예외처리도 해줘야 한다.
    - 1) l, r이 겹쳤을 때
    - 2) 1 차이날 때
    - 참고할 문제
        - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## End Case 예시
- end case
    - x x x x o o o o
    - x x x x 여기서 끝날 때
    - x x x x o o o o 여기서 끝날 때
    - 두 가지 엔드 케이스를 설명

```python
def getk(piles: List[int], h: int) -> int:
    def solve(m: int) -> int:
        # return times for eat all piles
        return sum(((pile - 1) // m + 1) for pile in piles)

    l, r = 1, max(piles)
    while l <= r:
        m = (l + r) // 2
        res = solve(m)
        if res > h:
            l = m + 1
        elif res <= h:
            r = m - 1
    return l
```


-----
## New

정리부터 하면, 네 노트에서 약간 섞여 있는 부분이 있어.

두 구현의 차이는 단순히 `while l < r` vs `while l <= r`가 아니라, **탐색 구간의 정의(invariant)** 가 다르다는 게 핵심이야.

### 1번: 반열린 구간 `[l, r)` — 경계 찾기용

```python
l, r = 0, len(a)

while l < r:
    m = (l + r) // 2

    if a[m] < x:
        l = m + 1
    else:
        r = m

return l
```

이건 정확히는:

> `a[i] >= x`가 처음으로 참이 되는 index를 찾아라

즉 `lower_bound`를 찾는 코드야.

핵심 invariant는:

```text
답 후보가 항상 [l, r) 안에 있다
```

여기서 `r = len(a)`도 가능한 이유는 답이 배열 밖, 즉 "모든 값보다 뒤"일 수도 있기 때문이야.

예를 들어:

```text
a = [1, 3, 5]
x = 7
```

이면 첫 `>= 7` 위치는 index `3`이야.

그래서 `r = n`으로 시작하는 게 자연스러워.

`a[m] < x`이면?

```text
m은 절대 답이 아님
m보다 왼쪽도 전부 답이 아님
```

그러니까:

```python
l = m + 1
```

반대로:

```text
a[m] >= x
```

라면 `m`이 **첫 번째 >= x**일 수도 있어.

그래서 `m`을 버리면 안 되고:

```python
r = m
```

이 되는 거야.

결국:

```text
l == r
```

이 될 때까지 후보 구간을 하나의 위치로 수렴시켜.

---

### 2번: 닫힌 구간 `[l, r]` — 정확한 값 찾기

```python
l, r = 0, len(arr) - 1

while l <= r:
    m = (l + r) // 2

    if arr[m] < x:
        l = m + 1
    elif arr[m] > x:
        r = m - 1
    else:
        return m

return -1
```

여기서는 invariant가:

```text
아직 확인하지 않은 후보가 [l, r] 안에 있다
```

야.

`arr[m] < x`라면 sorted array니까:

```text
0 ... m
```

은 전부 버릴 수 있어.

그래서:

```python
l = m + 1
```

`arr[m] > x`라면:

```text
m ... r
```

전부 버릴 수 있으니까:

```python
r = m - 1
```

여기서는 `m`을 직접 검사해서:

```python
arr[m] == x
```

면 바로 return하니까 `m` 자체를 버려도 돼.

---

## 네 노트에서 가장 중요한 오해

이 부분:

> 원소가 2개일 때 `r = m - 1` 하면 다른 원소를 못 볼 수 있다

이건 **standard binary search에서는 그렇지 않아.**

예:

```text
a = [1, 3]
x = 3
```

처음:

```text
l=0, r=1
m=0
a[m]=1 < 3
```

그래서:

```text
l = 1
```

다음:

```text
l=1, r=1
m=1
```

`3`을 검사하고 찾음.

반대로 `x=1`이면 첫 iteration에서 바로 찾고.

즉:

```python
while l <= r
```

를 정확히 쓰면 **원소 1개/2개에 대한 별도 예외처리가 필요 없어.**

네가 걱정한:

> `l == m == 0`이고 `r = m-1` 되면 index 1을 못 본다

상황은 `arr[m] > x`인 경우잖아.

예를 들어:

```text
[1,3]에서 x를 찾는데
m=0, arr[m]=1 > x
```

라면 `x < 1`인 거니까 index 1의 `3`은 볼 필요 자체가 없어.

sorted라는 성질 때문에 통째로 버리는 게 정당한 거야.

---

## 둘을 더 본질적으로 비교하면

### `[l, r]` 방식

```python
while l <= r:
```

목표:

```text
"x가 정확히 있나?"
```

매 iteration마다 `m`을 직접 검사해서:

```text
찾았으면 종료
아니면 m도 포함해서 한쪽 영역을 완전히 제거
```

그래서:

```python
l = m + 1
r = m - 1
```

둘 다 가능.

---

### `[l, r)` 방식

```python
while l < r:
```

목표:

```text
"조건이 false→true로 바뀌는 첫 위치가 어디인가?"
```

예:

```text
F F F F T T T T
        ^
      찾는 곳
```

`cond(m) == True`이면:

```text
m이 첫 True일 수도 있음
```

그래서:

```python
r = m
```

으로 남겨둬야 해.

---

## `Find Peak Element`는 조금 다른 케이스

이것도 흔히:

```python
l, r = 0, n - 1

while l < r:
    m = (l + r) // 2

    if nums[m] < nums[m + 1]:
        l = m + 1
    else:
        r = m

return l
```

을 쓰는데, 여기서는 `[l,r)`가 아니라 실질적으로 **닫힌 후보 구간 `[l,r]`를 하나로 수렴시키는 형태**라고 보는 게 더 정확해.

즉:

> `while l < r`이면 무조건 `[l,r)`다

는 건 아니야.

이게 네 노트에서 조금 위험한 부분이야.

`while` 조건만 보고 구간을 판단하면 안 되고:

```text
r 초기값이 n인가 n-1인가?
r = m 인가 m-1인가?
최종적으로 무엇을 찾는가?
```

를 같이 봐야 해.

---

## 제일 실전적인 구분법

나는 이렇게 외우는 걸 추천해.

### 정확한 값을 찾는다

```python
l, r = 0, n - 1

while l <= r:
    m = (l+r)//2

    if a[m] == target:
        return m
    elif a[m] < target:
        l = m+1
    else:
        r = m-1
```

`Search in Rotated Sorted Array`도 기본적으로 이 계열.

### 첫 번째 True / 최소 만족값을 찾는다

```python
l, r = ...

while l < r:
    m = (l+r)//2

    if condition(m):
        r = m
    else:
        l = m+1

return l
```

예를 들어:

```text
x x x x o o o o
        ^
     first True
```

이 패턴.

---

그리고 네 마지막 Koko 코드:

```python
l, r = 1, max(piles)

while l <= r:
    m = (l+r)//2

    if solve(m) > h:
        l = m+1
    else:
        r = m-1

return l
```

이것도 맞아.

재밌는 점은 이건 **경계 찾기인데도 `l <= r`를 쓴다**는 거야.

왜냐하면 여기서는 `m`을 검사한 뒤:

```text
불가능 → m 포함 왼쪽 버림
가능 → m 포함 오른쪽 버림
```

하고 마지막에:

```text
r < l
```

로 교차시켜서 `l`을 first True 위치에 놓는 방식이거든.

즉 결론적으로 제일 중요한 건:

> `값 찾기 = l<=r`, `경계 찾기 = l<r`  
> 라고 100% 외우면 안 돼.

더 정확한 기준은:

> **내 탐색 구간이 뭘 의미하고, `m`을 버릴 수 있는지, 종료했을 때 `l/r`가 무엇을 가리키는지**를 정의하는 것.

실전에서는 템플릿 2개만 확실히 외우면 돼:

```python
# exact search
while l <= r:
    ...
```

```python
# first True
while l < r:
    ...
```

그리고 Koko처럼 `first True`를 `l<=r`로 구현하는 변형도 있다는 정도로 이해하면 충분해.

돼. **경계 찾기도 `l <= r`로 충분히 구현 가능해.** 핵심은 마지막에 `l` 또는 `r`이 경계를 가리키도록 만드는 거야.

예를 들어 lower bound, 즉 첫 `a[i] >= x` 찾기:

```python
l, r = 0, len(a) - 1

while l <= r:
    m = (l + r) // 2

    if a[m] < x:
        l = m + 1
    else:
        r = m - 1

return l
```

예를 들어:

```text
a = [1, 3, 5, 7]
x = 4
```

종료하면:

```text
r = 1
l = 2
```

즉 경계 사이가:

```text
[1, 3] | [5, 7]
         ^
         l
```

이라서 `l=2`가 첫 `>=4` 위치야.

`x=5`여도 똑같이 `l=2`가 나와.

그래서 같은 lower bound를 두 방식으로 다 쓸 수 있어.

```python
# 방식 A: 수렴
l, r = 0, len(a)
while l < r:
    m = (l + r) // 2
    if a[m] < x:
        l = m + 1
    else:
        r = m
return l
```

또는:

```python
# 방식 B: 교차
l, r = 0, len(a) - 1
while l <= r:
    m = (l + r) // 2
    if a[m] < x:
        l = m + 1
    else:
        r = m - 1
return l
```

차이는 종료 모양이야:

```text
l < r 방식:
[l ... r]을 하나로 수렴
종료: l == r

l <= r 방식:
후보들을 전부 버리면서 두 포인터가 교차
종료: r < l
```

경계 찾기에서는 보통 종료 후:

```text
r = 마지막 False
l = 첫 True
```

가 돼.

그래서 네가 `l <= r` 방식이 더 익숙하면 **그걸로 통일해서 써도 전혀 문제 없어.** 오히려 exact search랑 boundary search 둘 다 같은 loop 형태를 쓰니까 외우기 편할 수 있어.
