from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int, input().split())

stk = deque(range(1,n+1))
jsps = []

while stk:
    for i in range(k-1):
        stk.append(stk.popleft())
    jsps.append(stk.popleft())
print(f"<{', '.join(map(str, jsps))}>")