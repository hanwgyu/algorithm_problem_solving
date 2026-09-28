# Solution 1 : 모든 조합에 대해 공약수 가지고 있는지 체크하고, Union-find로 합침.
# Time : O(N^2 * logM) (M은 리스트의 가장 큰 숫자),  Space : O(N)
# Time Limit Exceeded.

# Solution 2 : 각 숫자를 구성하는 소수들에 대한 set을 만든 후, set들을 하나씩 비교하며 합침.
# Time Limit Exceeded. 3792 ms

# Solution 3 : 각 숫자를 구성하는 소수들에 대한 set을 만든 후, 소수들을 Union-find로 합침.
# by 1), 3308ms -> 396ms

import math
from typing import Set

class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        """
        모든 숫자를 돌면서 직접 나눠보고 해당하는 K개에 대해 union-find를 함. 
        
        이미 합쳐진것들 제외하고?
        1) factor 하나가 K개의 원소에 등장했을때 K-1번만 해서 다 동일한 union으로 묶으면됨.

        다 돌면 너무 많은데. 한번이라도 연결된것들은 빼도 될텐데.
        2) 연결된 두 edge를 저장하고 그건 패스하고 진행.

        O(max(nums)*N)/ O(N)

        최적화 : 그냥 소인수분해를함.
        sqrt(max(nums))까지 소인수 분해하고, 소인수분해하면서 해당하는것들 저장해놓음.
        O(N*sqrt(max(nums))) / O(N)


        최적화 2: 
        아리스토텔리스의 체로 소수 구해놓고 이걸로만 계산하고, 제곱이 해당 숫자 소인수분해한값 보다 크면 더 진행안하고, 각 숫자마다 각자 진행하는거라는거지?
        """
        N = len(nums)
        factor_owner = defaultdict(set)
        for factor in range(2, int(sqrt(max(nums)))+1):
            for i in range(N):
                num = nums[i]
                while num % factor == 0:
                    num //= factor
                    factor_owner[factor].add(i)
                nums[i] = num
        
        for i, num in enumerate(nums):
            if num != 1:
               factor_owner[num].add(i)
        
        # union-find
        d = {i:i for i in range(N)}
        heights = {i:0 for i in range(N)}
        sizes = {i:1 for i in range(N)}
        def find(a: int) -> int:
            if d[a] != a:
                #path compression
                d[a] = find(d[a])
            return d[a]
        
        def union(a:int, b:int):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            ha, hb = heights[ra], heights[rb]
            if ha > hb:
                d[rb] = ra
                sizes[ra] += sizes[rb]
            elif ha < hb:
                d[ra] = rb
                sizes[rb] += sizes[ra]
            else:
                d[ra] = rb
                heights[rb] += 1
                sizes[rb] += sizes[ra]
        
        for _, owners in factor_owner.items():
            owners = list(owners)
            first_owner = owners[0]
            for owner in owners[1:]:
                union(first_owner, owner)
        return max(sizes.values())

                



class Solution:
    def findPrimeFactors(self, a: int) -> Set[int]:
        factor, prime_factors = 2, set()
        while a >= (factor * factor):
            if a % factor == 0:
                a //= factor
                prime_factors.add(factor)
            else:
                factor += 1
        prime_factors.add(a)
        return prime_factors

    def largestComponentSize_3(self, A: List[int]) -> int:
        def find(a: int) -> int:
            while a != d[a][0]:
                a = d[a][0]
            return a

        def union(a: int, b: int):
            ra, rb = find(a), find(b)
            if ra != rb:
                # 1) 큰 set에 작은 set을 union하도록 구현. find 비용 줄일 수 있음.
                if d[ra][1] > d[rb][1]:
                    ra, rb = rb, ra
                d[ra][0] = rb
                d[rb][1] += d[ra][1]

        d, values = {}, {}
        for a in A:
            # a의 prime factor들을 union 으로 연결
            s = list(self.findPrimeFactors(a))
            # a를 표현하는 값을 저장
            values[a] = s[0]
            for e in s:
                if not e in d:
                    d[e] = [e, 1]
            for i in range(len(s) - 1):
                union(s[i], s[i + 1])
        sizes = defaultdict(int)
        for a in A:
            sizes[find(values[a])] += 1
        return max(sizes.values())

    def largestComponentSize_2(self, A: List[int]) -> int:
        s = [[self.findPrimeFactors(a), 1] for a in A]
        i = 0
        # 겹치는 부분들을 합침
        while i < len(s):
            j = i + 1
            is_combined = False
            while j < len(s):
                if j != i and s[i][0].intersection(s[j][0]):
                    s[i][0].update(s[j][0])
                    s[i][1] += s[j][1]
                    s.pop(j)
                    is_combined = True
                else:
                    j += 1
            if not is_combined:
                i += 1
        return max(s, key=lambda e: e[1])[1]

    def largestComponentSize_1(self, A: List[int]) -> int:
        def checkCommonFactor(a: int, b: int) -> bool:
            for i in range(2, int(max(math.sqrt(min(a, b)), min(a, b))) + 1):
                if a % i == 0 and b % i == 0:
                    return True
            return False

        def find(a: int) -> int:
            while d[a][0] != a:
                a = d[a][0]
            return a

        def union(a: int, b: int):
            ra, rb = find(a), find(b)
            if ra != rb:
                d[ra][0] = rb
                d[rb][1] += d[ra][1]

        d = {}
        for a in A:
            d[a] = [a, 1]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                if checkCommonFactor(a, b):
                    union(a, b)
        return max(d.values(), key=lambda e: e[1])[1]
