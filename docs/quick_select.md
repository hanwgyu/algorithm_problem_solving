# Quick Select

- https://leetcode.com/problems/k-closest-points-to-origin/
- k개의 closest한 point들을 리턴. O(N) / O(1)에 가능.
- heap 쓰면 O(Nlogk) / O(k).

## quickSelect 구현

```python
import random
class Solution:
    # decreasing order로 sorting.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(l, r):
            pivot = random.randint(l, r)
            pos = partition(l, r, pivot)
            quickSort(l, pos - 1)
            quickSort(pos + 1, r)

        def partition(l, r, pivot):
            # pivot을 맨 오른쪽으로 이동
            nums[r], nums[pivot] = nums[pivot], nums[r]
            pivot = r
            # pivot 왼쪽부터 시작.
            r = r - 1
            while l <= r:
                if nums[l] >= nums[pivot]:
                    l += 1
                elif nums[pivot] >= nums[r]:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
            # 모두 sort하고 나면 pivot과 l을 swap.
            # pivot을 기준으로 왼쪽은 pivot보다 모두 크고, 오른쪽은 모두 작음.
            nums[l], nums[pivot] = nums[pivot], nums[l]
            return l

        l, r = 0, len(nums) - 1
        while True:
            pivot = random.randint(l, r)
            pos = partition(l, r, pivot)
            if pos < k - 1:
                l = pos + 1
            elif pos > k - 1:
                r = pos - 1
            else:
                return nums[pos]
```
