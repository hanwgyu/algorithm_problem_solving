# Study Roadmap

이 레포에서 이미 풀어둔 문제/정리 기준으로, 공부 순서와 추천 문제를 정리했다.  
기본기는 짧고 자주, 심화는 길게 반복하는 흐름으로 구성했다.

## 0. 빠른 정리 (이론)
- 시간/공간 복잡도: O(1), O(logN), O(N), O(NlogN), O(N^2) 기준으로 입력 크기 대비 가능 여부 판단.
- 정답 도출법: "상태(state) + 전이(transition) + 초기값(base)"로 문제를 분해.
- 불변식(invariant): 반복문/재귀에서 항상 유지되는 조건을 먼저 정하면 실수 감소.
- 최적화 패턴: 정렬 후 두 포인터, 누적합+해시, 단조 스택/큐, 이분 탐색 on answer.
- 그래프 선택: 가중치 없음은 BFS, 가중치 양수는 Dijkstra, 최단 경로 전부는 Floyd-Warshall.

## 1. 기초 → 중급 순서
1) 배열/문자열 + 해시
- 문서: [substrings](../docs/substrings.md), [palindrome](../docs/palindrome.md)
- 추천 문제: [Two Sum](../Leetcode/Two_Sum.py), [Group Anagrams](../Leetcode/Group_Anagrams.py), [First Unique Character](../Leetcode/First_Unique_Character_in_a_String.py)

2) 투 포인터 / 슬라이딩 윈도우
- 문서: [two_pointer](../docs/two_pointer.md)
- 추천 문제: [Two Sum II](../Leetcode/167.py), [Longest Substring](../Leetcode/3.py), [Minimum Window Substring](../Leetcode/76.py), [Max Consecutive Ones III](../Leetcode/1004.py)

3) 스택 / 큐
- 문서: [monotonic_stack](../docs/monotonic_stack.md)
- 추천 문제: [Valid Parentheses](../Leetcode/Valid_Parentheses.py), [Daily Temperatures](../Leetcode/Daily_Temperatures.py), [Largest Rectangle](../Leetcode/Largest_Rectangle_in_Histogram.py)

4) 링크드 리스트
- 문서: [linked_list](../docs/linked_list.md)
- 추천 문제: [Reverse Linked List](../Leetcode/Reverse_Linked_List.py), [Linked List Cycle](../Leetcode/Linked_List_Cycle.py), [Swap Nodes in Pairs](../Leetcode/Swap_Nodes_in_Pairs.py)

5) 이분 탐색
- 문서: [binary_search](../docs/binary_search.md)
- 추천 문제: [Find First and Last Position](../Leetcode/34.py), [Find Minimum in Rotated Array](../Leetcode/153.py), [Search in Rotated Sorted Array](../Leetcode/Search_in_Rotated_Sorted_Array.py)

6) 우선순위 큐(힙)
- 문서: [heap](../docs/heap.md)
- 추천 문제: [K Closest Points](../Leetcode/K_Cloest_Points_to_Origin.py), [Meeting Rooms II](../Leetcode/253.py), [Top K Frequent Words](../Leetcode/692.py)

7) 트리 기본
- 추천 문제: [Validate BST](../Leetcode/Validate_Binary_Search_Tree.py), [LCA of a Binary Tree](../Leetcode/Lowest_Common_Ancestor_of_a_Binary_Tree.py), [Binary Tree Right Side View](../Leetcode/Binary_Tree_Right_Side_View.py)

8) 그래프 기본 (BFS/DFS/Union-Find/Topo)
- 문서: [bfs](../docs/bfs.md), [graph](../docs/graph.md)
- 추천 문제: [01 Matrix](../Leetcode/542.py), [Number of Provinces](../Leetcode/547.py), [Course Schedule](../Leetcode/Course_Schedule.py), [Network Delay Time](../Leetcode/Network_Delay_Time.py)

9) DP 기본
- 문서: [lis](../docs/lis.md)
- 추천 문제: [Climbing Stairs](../Leetcode/Climbing_Stairs.py), [Coin Change](../Leetcode/Coin_Change.py), [Longest Palindromic Subsequence](../Leetcode/Longest_Palindromic_Subsequence.py), [Maximal Square](../Leetcode/Maximal_Square.py)

## 2. 심화 순서
10) 백트래킹 / 재귀 설계
- 문서: [backtracking](../docs/backtracking.md)
- 추천 문제: [Generate Parentheses](../Leetcode/Generate_Parentheses.py), [Permutations](../Leetcode/Permutations.py), [Sudoku Solver](../Leetcode/37.py)

11) 트라이
- 문서: [trie](../docs/trie.md)
- 추천 문제: [Implement Trie](../Leetcode/208.py), [Word Search II](../Leetcode/212.py), [Autocomplete System](../Leetcode/642.py)

12) 단조 스택/큐 심화
- 문서: [monotonic_stack](../docs/monotonic_stack.md)
- 추천 문제: [Daily Temperatures](../Leetcode/739.py), [Shortest Subarray With Sum](../Leetcode/862.py), [Count Submatrices With All Ones](../Leetcode/1504.py)

13) 세그먼트 트리 / 펜윅 트리
- 문서: [segment_tree](../docs/segment_tree.md), [fenwick_tree](../docs/fenwick_tree.md)
- 추천 문제: [Range Sum Query - Mutable](../Leetcode/307.py), [Range Module](../Leetcode/715.py)

14) 고급 그래프/DP
- 추천 문제: [Cheapest Flights Within K Stops](../Leetcode/787.py), [Shortest Path Visiting All Nodes](../Leetcode/847.py), [Stone Game III](../Leetcode/1406.py), [Stone Game IV](../Leetcode/1510.py)

## 3. 문제 풀이 시작 추천 순서 (빠른 시작용 15개)
1. [Two Sum](../Leetcode/Two_Sum.py)
2. [Valid Parentheses](../Leetcode/Valid_Parentheses.py)
3. [Two Sum II](../Leetcode/167.py)
4. [Longest Substring](../Leetcode/3.py)
5. [Daily Temperatures](../Leetcode/Daily_Temperatures.py)
6. [Reverse Linked List](../Leetcode/Reverse_Linked_List.py)
7. [Linked List Cycle](../Leetcode/Linked_List_Cycle.py)
8. [Find First and Last Position](../Leetcode/34.py)
9. [Find Minimum in Rotated Array](../Leetcode/153.py)
10. [Climbing Stairs](../Leetcode/Climbing_Stairs.py)
11. [Coin Change](../Leetcode/Coin_Change.py)
12. [01 Matrix](../Leetcode/542.py)
13. [Number of Provinces](../Leetcode/547.py)
14. [Course Schedule](../Leetcode/Course_Schedule.py)
15. [Range Sum Query - Mutable](../Leetcode/307.py)

## 4. 체크리스트 (문제 읽을 때 바로 쓰기)
- 입력 크기 N, M이 어느 정도인지부터 계산.
- 정렬/해시/투포인터/DP 중 어떤 패턴이 보이는지 30초 내에 가설.
- 엣지 케이스: 빈 배열, 길이 1, 중복 값, 음수/0.
- 시간 복잡도 후보 2~3개를 적고, 최적/차선안을 비교.
- 구현 전에 상태 정의(변수 의미)와 반복 불변식을 한 줄로 적기.

## 5. 면접 가이드 (요약)
- 문제를 들으면 바로 입력/출력/제약을 질문해서 명확히 하기.
- 코너 케이스를 미리 나열하고, 어떤 테스트로 확인할지 말하기.
- 시간/공간 복잡도 목표를 면접관에게 확인하기.
- 먼저 브루트포스 아이디어를 말하고, 최적화 방향을 연결하기.
- 계속 생각 과정을 말하기(면접관이 힌트를 줄 수 있음).
- 풀이가 길면 간단히만 공유하고, 코딩으로 넘어가기.
- 코드 라인은 50줄 내로 유지하는 연습을 하기.

## 6. 면접 중 풀이 순서 (템플릿)
1) 문제 정의 및 요구사항 확인\n
2) Naive/Optimal 접근 논의\n
3) 시간/공간 복잡도 분석\n
4) 메인 코드 + 간단 테스트 작성/디버깅

## 7. 참고 링크
- https://giunglee.notion.site/Live-Coding-Exercises-fe762939bc9846aca209fc715a5325a5
- https://codeinterview.io/
