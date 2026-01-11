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


## Palindrome + Rolling Hash 팁
- 문자열 s와 reverse(s)에 대해 같은 길이 구간의 해시를 비교하면 palindrome 후보를 빠르게 찾을 수 있다.
- 보통 이분 탐색(길이) + 해시 비교로 최장 palindrome 길이를 찾는 변형이 가능하다.
- 충돌 방지를 위해 2개의 MOD를 쓰거나, 해시가 같을 때 실제 문자열을 한 번 더 확인한다.
- 구현 시 prefix hash와 pow 배열을 미리 만들어두면 O(1)로 구간 해시를 계산할 수 있다.

```python
# hash(l, r) = (prefix[r] - prefix[l] * pow_base[r-l]) % MOD
```
