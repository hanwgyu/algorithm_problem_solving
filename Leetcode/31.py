# Solution : 뒤의 자리부터 Permutation의 맨 끝인지를 확인 (이전 자리까지의 가장 큰 숫자와 현재 자리의 숫자를 비교)
# Permutation 맨끝이 아닌 시점을 기준으로 자기보다 큰 수가 위치하는 자리와 스왑하고
# 이전 자리들은 오름 차순으로 정렬시킴. (내림차순 -> 오름차순으로)
# Time : O(N), Space: O(1)


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        permutation을 구하는 과정.
        뒤에서부터 숫자가 작아지는 지점을 pivot으로 잡고, 그것보다 그다음 큰 값을 뒤쪽에서 찾아서 그것과 swap함.
        그러면 뒤쪽은 작아지는 순서로 여전히 존재하고, 그걸 앞뒤 뒤집으면 됨.
        이거 계속하면 계속 다음게 구해짐.

        이건 외워야하는 수준.
        """
        N = len(nums)
        i = N-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # swap pivots
        if i > 0:
            a = i-1
            b = i
            while b < N and nums[b] > nums[a]:
                b += 1
            nums[a], nums[b-1] = nums[b-1], nums[a]
        # reverse
        j = N-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1



        

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N, i, m = len(nums), len(nums) - 1, float("-inf")
        while i >= 0 and nums[i] >= m:
            m, i = max(m, nums[i]), i - 1
        # find bigger element location and swap with target
        if i >= 0:
            j = i + 1
            while j < N and nums[j] > nums[i]:
                j = j + 1
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
        # ordering
        i, j = i + 1, N - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        뒤에서부터 시작해서 값이 감소할때까지 움직이고, 그 위치에서 이전 보다 큰 값을 찾고, 뒤집는다.

        1234 1243 1324 1342 1423 1432 2134 2143 2314 2341
        
        2431 
        """
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = nums[::-1]
            return
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:len(nums)] = nums[i:len(nums)][::-1]
