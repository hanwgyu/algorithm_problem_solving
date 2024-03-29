
# 자기 보다 오른쪽에 있는 원소들만 가지고 내림 차순으로 sorting 했을때 오른쪽부터의 index.
# 전체로 합쳐지는 순간에서 왼쪽 원소일 경우에만 남은 오른쪽 배열의 원소 갯수로 값을 업데이트함.
# 오른쪽 원소인 경우에는 이미 오른쪽에 있어서 문제에서 고려하는 케이스가 아니다.
# 첫 index를 저장하여 결과를 구할때 사용.

# REMIND : 천재적인 아이디어. 어려워. mergesort 구현도 pop을 써서 깔끔함.

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        def mergesort(A):
            """
                오름 차순으로 정렬.
            """
            half = len(A) // 2
            if half:
                L, R = mergesort(A[:half]), mergesort(A[half:])
                for i in reversed(range(len(A))):
                    if not R or L and L[-1][1] > R[-1][1]:
                        res[L[-1][0]] += len(R)
                        A[i] = L.pop()
                    else:
                        A[i] = R.pop()
            return A
        mergesort(list(enumerate(nums)))
        return res
        

        class Solution:
            
            
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        내림 차순으로 mergesort 를 진행하면서.
        두 array를 merge 시 왼쪽 array에 있는 원소가 합쳐지는 시점에 오른쪽 array에 남은 원소의 갯수를 더한다.
        총 갯수가 합쳐진 array에서 특정 원소보다 작고 오른쪽에 있는 갯수.
        """
        N = len(nums)
        res = [0 for _ in range(N)]
        def merge_sort(a: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
            """
            내림 
            """
            if len(a) < 2:
                return a
            half = len(a) // 2
            al, ar = merge_sort(a[:half]), merge_sort(a[half:])
            l, r = 0, 0
            while l < len(al) and r < len(ar):
                if al[l][1] > ar[r][1]:
                    a[l+r] = al[l]
                    res[al[l][0]] += len(ar)-r
                    l += 1
                else:
                    a[l+r] = ar[r]
                    r += 1
            while l < len(al):
                a[l+r] = al[l]
                l += 1
            while r < len(ar):
                a[l+r] = ar[r]
                r += 1
            return a

        merge_sort(list(enumerate(nums)))
        return res
