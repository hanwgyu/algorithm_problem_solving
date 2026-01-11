# Palindrome

## 기본 아이디어
- 길이가 홀수인 것과 짝수인 것을 나눠서 생각
    - `aba`
    - `abba`
- 양 끝에 같은 원소가 추가될 때 더 커진 palindrome이 된다.
- 예시: https://leetcode.com/problems/palindrome-partitioning-ii/

## Manacher's Algorithm
- String 내에 존재하는 모든 palindrome의 개수를 O(N)에 구함.
- 특정 위치에서의 최대 palindrome 길이를 저장해나아가고, center를 기준으로 mirror이기 때문에 반대편 위치에서의 최소 palindrome 길이를 계산하지 않고 구할 수 있다.
    - ex) aba c abac...이면 두번째 b 위치의 최대길이 3을 그대로 이용해 여섯번째 b의 최소 길이를 3으로 두는데 사용한다.
- Rightmost R 가 바귀면 그값과 Center C 위치를 계속 업데이트 해나아가고, 대칭이 되는 위치의 최대 palindrome 길이가 Rightmost 에 못미치면, mirror이므로 이미 앞에서 검증한 값과 같아서 더이상 palindrome인지를 체크할 필요가 없다. 그냥 그다음으로 넘어가면 됨.
- Refer
  - https://leetcode.com/problems/longest-palindromic-substring/description/
  - [Code](Leetcode/Longest_Palindromic_Substring.py)


## Rolling Hash - Rabin Karp
- 문자열 매칭 알고리즘.
- 각 문자를 표현하는 숫자를 이용해 전체 문자열을 숫자로 변환하고, 각 자리수에 pow(BASE, i)를 곱해서 더한다. 최대 범위값인 MOD값을 통해 나눈다.
- 두 값이 동일한지를 통해 문자열을 매칭한다. (값이 같은데 문자열이 다른 경우가 존재할 수 있기 때문에, 값을 한번 더 더블체크한다. 빈번하지 않기에 시간 복잡도에는 변화가 없다.)
- 긴 문자열을 매치할 때 한 글자씩 이동하면서 겹치는 부분을 그대로 사용하고, 추가되고 제거되는 문자 두 개만 계산. - Rolling Hash
- O(N)
- https://github.com/hanwgyu/algorithm_problem_solving/blob/master/Leetcode/1044.py
