# BOJ 17298 오큰수
# 날짜: 2026-04-05
# 분류: 스택, 단조 스택
# 핵심 아이디어:
# - 스택에는 "오큰수를 아직 못 찾은 인덱스" 저장
# - 현재 값이 스택 top보다 크면 → 그 원소의 오큰수 확정
# - 각 원소는 push/pop 최대 1번 → O(N)
# 오큰수는 아래처럼 풀면 시간초과 남 → O(N^2) 

# import sys
# input = sys.stdin.readline

# N = int(input())
# s = list(map(int, input().split()))
# ans = []

# for i in range(N):
#     tar = s[i]
#     found = False
    
#     for j in range(i+1,N):
#         if tar < s[j]:
#             found = True
#             ans.append(s[j])
#             break
#     if not found:
#         ans.append(-1)

# print(*ans)

# BOJ 17298 오큰수

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = [-1] * N
stk = []

for i in range(N):
    # 스택에 남아있는 인덱스들은 "아직 오큰수를 못 찾은 상태"
    # 현재 값(arr[i])이 스택 top보다 크면 → 그 top의 오큰수는 지금 값
    while stk and arr[stk[-1]] < arr[i]:
        ans[stk.pop()] = arr[i]  # 오큰수 확정

    # 현재 인덱스는 아직 오큰수를 모르는 상태라 스택에 넣음
    stk.append(i)

print(*ans)