"""
엄청 까다로운 Bianry Search 문제. 두가지 템플릿으로 구현할때 방법이 다르고, 예외 처리를 유의깊게 해줘야 한다.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N-1
        while l < r:
            m = (l+r)//2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]
    
class Solution:
    def findMin(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l <= r:
            m = (l+r)//2
            if m > 0 and A[m] < A[m-1]:
                return A[m]
            if A[m] > A[r]:
                l = m+1
            else:
                r = m-1
        return A[l]
        
        
        
    
    def findMin1(self, A: List[int]) -> int:
        lo, hi = 0, len(A)-1
        while lo < hi:
            mid = (lo+hi)//2
            if A[mid] > A[hi]:
                lo = mid+1
            else:
                hi = mid
        return A[lo]
