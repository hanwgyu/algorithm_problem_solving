# Segment Tree

- Array가 주어질 때 특정 범위의 연속된 Subarray의 min값을 빠르게 구할 수 있음.
- 아이디어: 일종의 merge sort.
- range를 반씩 쪼개서 미리 2N-1 공간에 저장해놓고, 찾을 때도 반씩 쪼개가면서 찾음.

## Complexity
- Build: O(N) / O(N)
- Query: O(logN)
- Update: O(logN)

## 구현 방법
- 트리를 array로 구현
    - 자세한 링크: https://www.notion.so/Segment-Tree-f9b8cb797a6d4c7e95eaf02167bc586a?pvs=21
- Node라는 객체 생성해서 풀기
    - https://leetcode.com/problems/range-sum-query-mutable/discuss/75784/Python%3A-Well-commented-solution-using-Segment-Trees
- array인데 더 쉬운 구현
    - https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
