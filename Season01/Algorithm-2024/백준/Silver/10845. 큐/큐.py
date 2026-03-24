import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
stk = deque()

for i in range(N):
    ord = input().split()
    k = ord[0]

    if k == 'push':
        stk.append(ord[1])
    elif k == 'pop':
        if stk:
            print(stk.popleft())
        else:
            print('-1')
    elif k == 'size':
        print(len(stk))
    elif k == 'empty':
        print(1 if not stk else 0)
    elif k == 'front':
        if stk:
            print(stk[0])
        else:
            print('-1')
    elif k == 'back':
        if stk:
            print(stk[-1])
        else:
            print('-1')