from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
que = deque()

for i in range(n):
    ord = list(input().split())
    if len(ord) > 1:
        que.append(ord[1])
    elif ord[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print('-1')
    elif ord[0] == 'size':
        print(len(que))
    elif ord[0] == 'empty':
        if que:
            print('0')
        else:
            print('1')
    elif ord[0] == 'front':
        if que:
            print(que[0])
        else:
            print('-1')
    elif ord[0] == 'back':
        if que:
            print(que[-1])
        else:
            print('-1')