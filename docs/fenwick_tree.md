# Fenwick Tree (Binary Indexed Tree)

- Segment Tree와 쓰이는 부분은 똑같고, 공간복잡도와 시간복잡도도 동일하다.
- 그러나 공간이 약간 적게 들고 구현이 더 간단하다.
- Build: O(N) / O(N), Query: O(logN), Update: O(logN)
- N+1 만큼의 공간만 쓴다.
- 그러나 심각한 단점이 있다.
    - Sum이나 곱셈은 구할 수 있지만 max는 구할 수 없다. (역연산이 불가능하기 때문)
    - Tree에 범위를 잘 잡은 prefix sum N+1개를 저장해놓고, 차이를 통해 값을 구하는 방식이기 때문.
- prefix sum을 저장해놓고 사용하는 방식.
