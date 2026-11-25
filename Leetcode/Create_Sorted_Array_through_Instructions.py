class FenwickTree:
    def __init__(self):
        self.N = 10**5
        self.arr = [0] * (self.N+1)

    def query(self, i: int) -> int:
        """
        1-i
        """
        res = 0
        while i > 0:
            res += self.arr[i]
            lowbit = i & -i
            i -= lowbit
        return res

    def update(self, i: int, diff: int):
        while i <= self.N:
            self.arr[i] += diff
            lowbit = i & -i
            i += lowbit

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        가장 쉬운 방법: insert하는 위치를 찾을때 binary search하고 insert가 O(N)이라서 총 O(N^2)/O(1)

        고민1: insert에 비용이 안들어야함. doubly linked list로 O(1). 안됨
        고민2: 정렬된 리스트를 유지하지말고 ???? segment tree, binary index tree
        개수를 저장하고 i를 insert할때 fenwick tree로 1-i-1, i+1-max 까지의 cnt를 구함.
        """
        tree = FenwickTree()
        res = 0
        for i in instructions:
            # query 1 - (i-1)
            l = tree.query(i-1)

            # query i+1-max
            r = tree.query(10**5) - tree.query(i)

            res += min(l, r)
            # update
            tree.update(i, 1)
        
        return res % (10**9+7)


---
# Solution 1 : binary search 한후 add
# Time : O(N^2), Space : O(N).
# Time Limit Exceeded


# Solution 2 : binary index tree. instruction의 갯수를 업데이트해나아감.
# Time : O(MlogM). Space: O(M) # M: max(Instructions)

import bisect


class binaryIndexTree:
    def __init__(self, n: int):
        """ O(1), O(N)  """
        self.a = [0 for _ in range(n + 1)]

    def update(self, i: int, val: int):
        """ O(logN) """
        i += 1
        while i < len(self.a):
            self.a[i] += val
            i += i & -i

    def getSum(self, i: int, j: int) -> int:
        """ O(logN) """

        def getSumFromRoot(i: int) -> int:
            ret = 0
            i += 1
            while i > 0:
                ret += self.a[i]
                i -= i & -i
            return ret

        return getSumFromRoot(j) - getSumFromRoot(i - 1)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        bit = binaryIndexTree(m + 1)
        ans = 0
        for i, e in enumerate(instructions):
            ans += min(bit.getSum(0, e - 1), bit.getSum(e + 1, m))
            bit.update(e, 1)
        return ans % (pow(10, 9) + 7)

    def createSortedArray_1(self, instructions: List[int]) -> int:
        a = [instructions[0]]
        d = {instructions[0]: 1}
        ans = 0
        for i in range(1, len(instructions)):
            e = instructions[i]
            j = bisect.bisect_left(a, e)
            if j < len(a) and a[j] == e:
                ans += min(sum(d[e] for e in a[:j]), sum(d[e] for e in a[j + 1 :]))
                d[e] += 1
            else:
                ans += min(sum(d[e] for e in a[:j]), sum(d[e] for e in a[j:]))
                a.insert(j, e)
                d[e] = 1
        return ans % (pow(10, 9) + 7)
