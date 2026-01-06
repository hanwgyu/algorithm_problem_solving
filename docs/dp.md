# Dynamic Programming

## 핵심 아이디어
- 큰 문제를 작은 문제로 나누고, 작은 문제의 답을 저장해 중복 계산을 피한다.
- 상태(state) + 전이(transition) + 초기값(base) + 계산 순서(order)를 먼저 정의한다.

## 템플릿
1) 상태 정의: dp[i], dp[i][j]가 의미하는 바를 한 줄로 명확히 적기
2) 전이: 이전 상태에서 현재 상태로 넘어오는 규칙
3) 초기값: dp의 시작값
4) 계산 순서: 의존성이 해결되는 순서로 채우기
5) 답: dp에서 무엇을 리턴할지 결정

## Top-Down vs Bottom-Up
- Top-Down: 재귀 + 메모이제이션, 구현이 직관적이지만 스택 깊이 주의
- Bottom-Up: 반복문으로 채우기, 스택 문제 없음, 순서 설계가 중요

## 대표 패턴
- 1D DP: dp[i]가 이전 몇 칸(dp[i-1], dp[i-2])에만 의존
- 2D DP: 문자열, 격자 문제에서 자주 등장 (LCS, 편집 거리 등)
- Knapsack: "넣는다/안 넣는다" 선택으로 전이
- Interval DP: 구간을 늘려가며 계산 (burst balloons 등)

## 복잡도 최적화
- 상태 수: O(N) 또는 O(N^2)인지 먼저 계산
- 전이 비용을 줄이기 위해 prefix sum, monotonic queue, bitset 등을 고려
- 2D -> 1D로 줄일 수 있는지 확인 (이전 행/열만 참조할 때)
