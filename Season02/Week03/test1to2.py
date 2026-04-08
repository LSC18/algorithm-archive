# BOJ 1158 요세푸스 문제 / BOJ 17298 오큰수
# 날짜: 2026-04-06
# 분류: 큐(덱), 스택(단조 스택)
# 핵심 아이디어:
# [1158 요세푸스]
# - 원형 구조에서 K번째마다 제거
# - 인덱스 갱신 (idx = (idx + K - 1) % len)
# - 또는 deque rotate로 구현 가능
#
# [17298 오큰수]
# - 스택에는 "오큰수를 아직 못 찾은 인덱스" 저장
# - 현재 값이 스택 top보다 크면 → 해당 인덱스의 오큰수 확정
# - 각 원소는 push/pop 최대 1번 → O(N)


# BOJ 17298 오큰수
import sys
input = sys.stdin.readline

N = int(input())
# 4
arr = list(map(int, input().split()))
# 3 5 2 7

ans = [-1] * N
stk = []

for i in range(N):
    while stk and arr[stk[-1]] < arr[i]:
        ans[stk.pop()] = arr[i]
    
    stk.append(i)

print(*ans)


# BOJ 1158 요세푸스
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

s = list(range(1, N+1))
ans = []
start = 0

while s:
    start = (start + K - 1) % len(s)
    ans.append(s.pop(start))

print("<" + ", ".join(map(str, ans)) + ">")