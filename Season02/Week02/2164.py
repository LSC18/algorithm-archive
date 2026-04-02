# BOJ 2164 카드2
# 날짜: 2026-04-02
# 분류: 큐, 덱, 시뮬레이션
# 핵심 아이디어:
# - 1부터 N까지 카드 덱 구성
# - 맨 위 카드를 버린 후, 다음 카드를 덱의 뒤로 이동
# - 이 과정을 카드가 1장 남을 때까지 반복
# - 마지막에 남은 카드 출력
# 시간복잡도: O(N)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
s = deque(list(range(1,N+1)))

while len(s) > 1:
    s.popleft()
    s.rotate(-1)

print(s[0])