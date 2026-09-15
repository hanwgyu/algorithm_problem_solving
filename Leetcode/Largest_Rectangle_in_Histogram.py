# Solution 0 : heuristics. O(N^2), O(1)

# Solution 1 : 값이 커지면 Stack에 저장, 작아지면 Stack에서 빼서 최대값 계산.
# Stack에서 빼고 새로운 값을 추가할때 i값을 stack에 있던 값들을 고려해 설정.
# Time : O(N), Space : O(N)



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        increasing stack 저장
        저장할때 (높이, indedx) 저장하고, 덮어씌울때는 이전꺼의 index를 사용하게 해서 넓이가 이전인덱스까지 사용될수 있게함
        그리고 없어질때 넓이를 계산함.
        O(N) / O(N)
        """
        st = [(0,-1)] # height, index
        heights.append(0)
        res = 0
        for i, h in enumerate(heights):
            last_index = i
            while st and st[-1][0] >= h:
                th, last_index = st[-1]
                area = (i-last_index) * th
                if  area > res:
                    res = area
                st.pop()
            st.append((h, last_index))
        return res
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        s, ans = [], 0
        for i, h in enumerate(heights):
            if not s or s[-1][0] < h:
                s.append((h, i))
            elif s[-1][0] > h:
                new_i = i
                while s and s[-1][0] > h:
                    (old_h, old_i) = s.pop()
                    ans = max(ans, (i - old_i) * old_h)
                    new_i = old_i
                s.append((h, new_i))
        while s:
            (old_h, old_i) = s.pop()
            ans = max(ans, (len(heights) - old_i) * old_h)
        return ans
