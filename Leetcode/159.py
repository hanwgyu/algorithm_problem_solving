class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding window. 최적화. 동일한 문자의 마지막 index를 저장.
        
        O(N) / O(1)
        """
        d = {}
        i = ans = 0
        for j, c in enumerate(s):
            d[c] = j
            if len(d.keys()) > 2:
                # 문자 하나를 없애야함.
                # 현재 포함된 여러 문자들 중, 마지막 index가 가장 작은 문자를 제거하여 길이를 제일 길게 만듬.
                i_del = min(d.values())
                del d[s[i_del]]
                i = i_del+1
            ans = max(ans, j-i+1)
        return ans