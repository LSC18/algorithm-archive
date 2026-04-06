
# 오큰수 복습 17298

# import sys
# input = sys.stdin.readline

# N = int(input())
# # 4
# arr = list(map(int, input().split()))
# # 3 5 2 7

# ans = [-1] * N
# stk = []

# for i in range(N):
#     while stk and arr[stk[-1]] < arr[i]:
#         ans[stk.pop()] = arr[i]
    
#     stk.append(i)

# print(*ans)

# ----------------------------

# 요새푸스 문제 1158 
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
