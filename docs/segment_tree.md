# Segment Tree

- Array가 주어질 때 특정 범위의 연속된 Subarray의 min값을 빠르게 구할 수 있음.
- 아이디어: 일종의 merge sort.
- range를 반씩 쪼개서 미리 2N-1 공간에 저장해놓고, 찾을 때도 반씩 쪼개가면서 찾음.

## Complexity
- Build: O(N) / O(N)
- Query: O(logN)
- Update: O(logN)

## 구현 방법
- 트리를 array로 구현
    - 자세한 링크: https://www.notion.so/Segment-Tree-f9b8cb797a6d4c7e95eaf02167bc586a?pvs=21
- Node라는 객체 생성해서 풀기
    - https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python%3A-Well-commented-solution-using-Segment-Trees
- array인데 더 쉬운 구현
    - https://www.geeksforgeeks.org/segment-tree-efficient-implementation/


## 자세히

**Segment Tree**

https://www.youtube.com/watch?v=ZBHKZF5w4YU

- Array가 주어질때 특정 범위의 연속된 Subarray의 min값을 빠르게 구할수 있음. (O(logN))

Array로 구현.  O(N) 공간이 필요함.

### 트리 구조

- Array 원소들이 Tree의 Leaf가 되고, 위로 올라가면서 노드들은 Leaf들을 합친 특정 구역의 min값을 표현함.
- 반씩 나눠서 모든 원소를 Leaf로 설정함. 그 위로 올라가면서 연산 (min)값을 각 노드에 저장. 각 노드가 표현하는 범위는 Leaf에서부터 올라오면서 합치면 알 수 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2506dc9-aad8-457a-af16-8afa9a65ae6b/Untitled.png)

### **값 찾기 (특정 범위의 최솟값을 찾을때 )**

1. Totally Overlap : 트리 노드의 범위([1,4])가 찾고자하는 구역([1,5])에 완전히 속하면 **해당 노드의 값을 가지고** 리턴. 바로 올라가서 계산
2. Partially Overlap : 트리 노드의 범위([1,5])와 찾고자하는 구역([1,4])이 **일부가 겹치면 트리노드의 왼쪽, 오른쪽 자식을 모두 내려가서** 다시 찾음
3. No Overlap : 현재 노드의 값으로는 도움이 안됨. float('inf') 리턴하고 위로 올라감.

각 구역에서 min값을 계산하면서 올라와서 최종적으로 Root에서 min값을 계산.

postorder로 돌고, min 값을 계산함.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b38c114c-7075-489f-a678-ec089d55e349/Untitled.png)

### 1. **생성할때**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64bd5c74-6a2c-4b70-82b4-b68660dbabda/Untitled.png)

- (N x 2 - 1) 개의 원소가 필요하고(N 을 1로 줄이는 것과 동일하기때문), Array로 구현한다.
- tree의 root부터 순차적으로 array에 저장하는 방식.
- Child, parent 의 위치 구하기
    - child : 2i+1, 2i+2 가 left, right child가 됨.
    - parent : (i-1)//2가 parent가 됨.
- postorder로 dfs를 돌면서 가장 leaf의 값부터 채운 후, 위로 올라오면서 min값을 계산해 저장해나아감.

```python
def build(low: int, high: int, pos: int):
    """
    low~high 까지가 array내 인덱스 범위를 표현함.
    pos 는 segtree 내 인덱스.
    low==high일때 해당 pos에 값을 저장.
    """
    if low == high:
        segtree[pos] = array[low]
        return
    mid = (low+high)//2
    build(low, mid, 2*pos+1)
    build(mid+1, high, 2*pos+2)
    segtree[pos] = min(segtree[2*pos+1], segtree[2*pos+2])

```

```python
N = len(array)
segtree = [0 for _ in range(4*N)]
build(0, N-1, 0)
```

### 2. 값 찾기 함수

```python
def find(low: int, high: int, pos: int, target_low: int, target_high: int) -> int:
    # total overlap (target 범위 (target_low~target_high)가 tree 원소의 범위(low~high)를 포함함. 그냥 그대로 쓰면됨.)
    if low <= target_low and target_high <= high:
        return segtree[pos]
    # No overlap (tree 원소의 범위와 target 범위가 완전히 어긋남. 그냥 무한대를 리턴.)
    elif target_high < low or high < target_low:
        return float('inf')
   # Partial overlap (일부 겹침. left, right child로 이동한 후 min을 리턴.)
    mid = (low+high) // 2
    return min(find(low, mid, 2*pos+1, target_low, target_high), find(mid+1, high, 2*pos+2, target_low, target_high))
```

```python
find(0, N-1, 0, target_low, target_high)
```

### 3. 업데이트

- array의 값이 업데이트 되면, 해당 index를 포함하는 모든 tree의 node도 업데이트 필요.
- 트리 생성과 동일하게 구현, 예외처리만 추가함.
- log(N)만큼 걸림.

```python
def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        def updateInTree(low, high, pos, index):
            if index < low or high < index:
                return
            if low == high:
                self.segment_tree[pos] = self.nums[low]
                return 
            mid = (low+high) // 2
            updateInTree(low, mid, 2*pos+1, index)
            updateInTree(mid+1, high, 2*pos+2, index)
            self.segment_tree[pos] = self.segment_tree[2*pos+1] + self.segment_tree[2*pos+2]
        updateInTree()
```
