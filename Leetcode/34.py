class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return l
        
        def binary_search_right(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] <= target:
                    l = m+1
                else:
                    r = m-1
            return l
        
        #i, j = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        i, j = binary_search_left(nums, target), binary_search_right(nums, target)
        return [i, j-1] if i != j else [-1, -1]


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        def find_leftmost(nums: List[int], target: int) -> int:
            l, r = 0, N # 여기도 N을 씀.
            while l < r:
                m = (l+r)//2
                if nums[m] >= target:
                    r = m
                else:
                    l = m+1
            return l
        def find_rightmost(nums: List[int], target: int) -> int:
            """
            target보다 큰 숫자를 나타내는 위치를 리턴
            """
            l, r = 0, N # 여기도 N을 씀.
            while l < r:
                m = (l+r)//2
                if nums[m] > target:
                    r = m
                else:
                    l = m+1
            return l
        ans_l, ans_r = find_leftmost(nums, target), find_rightmost(nums, target)-1
        print(ans_l, ans_r)
        if ans_l <= ans_r < N and nums[ans_l] == nums[ans_r] and nums[ans_l] == target:
            return [ans_l, ans_r]
        return [-1,-1]
