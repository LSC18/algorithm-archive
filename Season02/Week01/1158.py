# BOJ 1158 요세푸스 문제
# 날짜: 2026-03-26
# 분류: 원형 배열, 구현
# 핵심 아이디어:
# - 리스트를 원형 구조처럼 사용
# - 현재 위치에서 K번째 사람 제거 → (start + K - 1) % len(stk)
# - 제거 후 다음 시작점은 현재 인덱스 유지 (자동으로 다음 원소로 이어짐)
# - 리스트 길이가 줄어드므로 매번 len(stk) 기준으로 인덱스 계산
# 시간복잡도: O(N^2) (pop(index)로 인한 shift 발생)
#
# 추가:
# - deque.rotate 방식도 가능하지만, 본 구현이 실측에서 더 빠른 결과를 보임

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

stk = []
start = 0
ans = []

for i in range(N):
    stk.append(i+1)

while stk:
    start = (start + K - 1) % len(stk)
    ans.append(stk.pop(start))

print("<" + ", ".join(map(str, ans)) + ">")

# from collections import deque
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())

# dq = deque(range(1, N+1))
# ans = []

# while dq:
#     dq.rotate(-(K-1))
#     ans.append(dq.popleft())

# print("<" + ", ".join(map(str, ans)) + ">")