# Time : O(logN), Space : O(1)
# 범위 설정하는 것이 상당히 까다로움. 여러번 시행착오를 거쳐 해답을 찾아냈음.


# m을 l, r과 비교하면서 rotated된걸을 확인해서 진행
# <=로 할지 <로 할지, r = m 으로할지, r = m-1로 할지 매우 어려움. 정형화 되어있는게 아니라 로직에 따라 결정을 해야함.
# 이 경우에는 매우우우우우어렵다..........ㅠㅠ

# Solution 2 :
# if 왼쪽 부분이 monotonically increasing => pivot이 오른쪽에 있다
#   if left <= target < mid -----> 오른쪽 절반 날림
#   else  -----> 왼쪽 절반 날림
# else 오른쪽 부분이 monotonically increasing => pivot이 왼에 있다
#   if mid < target <= right ---> 왼쪽 절반 날림
#   else ----> 오른쪽 절반 날림

"""
 Solution 3 : 비교하는 값을 변경해서 일반 binary search하는 것처럼 동작시킨다.

[12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

1. 17을 찾을때
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

2. 7을 찾을때
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

실제 array를 변경하는게 아니라 비교하는 mid 값을 조건에 따라 변경하자.
1. mid가 target과 다른 열에 있고,  mid < target -----> inf로 변경
2. mid가 target과 다른 열에 있고, mid > target -----> -inf로 변경
3. mid가 target과 같은 열에 있음 -----> 그대로 둠

다른 열에 있는지? ----> num0 <=  target != num0 <= mid

사이즈 2일때 예외 케이스 고려
nums  t
[1,3] 1 같은열   -> 로직은 mid=mid
[1,3] 3 같은열   -> 로직은 mid=mid
[3,1] 1 다른열   -> 로직은 mid=float('-inf')
[3,1] 3 다른열   -> 이부분 로직이 mid=mid 로 잘못처리되나 동작에 문제 없음 (바로 리턴)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        before_pivot = (target >= nums[0])
        # if true, set float('inf') if num <= nums[N].
        # if false, set float('-inf') if nums[0] <= num
        l, r = 0, N-1
        while l <= r:
            m = (l+r) // 2
            num = nums[m]
            if before_pivot and num < nums[0]:
                num = float('inf')
            elif not before_pivot and num >= nums[0]:
                num = float('-inf')
            if num > target:
                r = m-1
            elif num < target:
                l = m+1
            else:
                return m
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            n = nums[m]
            before_pivot = (target >= nums[0])
            if n >= nums[0]: # m is in before pivot
                if n < target:
                    l = m+1
                elif n > target and before_pivot:
                    r = m-1
                elif n > target and not before_pivot:
                    l = m+1
                else:
                    return m
            else: # m is in after pivot
                if n < target and before_pivot:
                    r = m-1
                elif n < target and not before_pivot:
                    l = m+1
                elif n > target:
                    r = m-1
                else:
                    return m         
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        after_pivot = (target < nums[0])
        while l <= r:
            m = (l+r)//2
            if after_pivot:
                n = nums[m] if nums[m] < nums[0] else float('-inf')
            else:
                n = nums[m] if nums[m] >= nums[0] else float('inf')
            if n < target:
                l = m+1
            elif n > target:
                r = m-1
            else:
                return m
        return -1

    def search_2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # 이부분을 < 로하면 '[3,1], 1'을 통과 못함... 이게 까다로운 부분이다.
                # m이 //2로 계산하기 때문에 원소 갯수가 2개로 작으면 l==m이 되고,
                # 조건문이  r= m-1로 진행될경우  그다음에 바로 while문을 빠져나온다. 근데 이러면 1인 부분을 체크할 수 없다.
                # 최대한 l을 변경하는 방식으로 진행되야 while문을 끝내지 않고 체크를 한번 더할 수 있다.
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

    def search_1(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # pivot이 존재하지 않는 경우
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            # pivot이 m 뒤쪽에 존재하는 경우
            elif nums[l] < nums[m]:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # pivot이 m 앞쪽에 존재하는 경우
            elif nums[l] > nums[m]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            # l과 m이 같은 경우
            else:
                l = m + 1
        return l if nums and nums[l] == target else -1
