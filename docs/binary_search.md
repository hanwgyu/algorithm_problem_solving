# Binary Search

## 구현 방식
아래와 같이 두가지 방식으로 구현할 수 있다.
```py
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    m = 0

    while low < high:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m
        else:
            return m
    return -1
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
