# BOJ 10845 큐
# 날짜: 2026-03-25
# 분류: 큐, 구현
# 핵심 아이디어:
# - 배열 기반 큐 구현
# - front, rear 포인터 사용
# - push는 rear 증가, pop은 front 증가
# - 원형 큐로 overflow 방지
# 시간복잡도: O(1)

import sys
input = sys.stdin.readline

T = int(input())
size = 2*T
arr = [0]*size
front = rear = size // 2

for _ in range(T):
    cmd = input().split()
    
    if cmd[0] == 'push':
        arr[rear] = cmd[1]
        rear = (rear + 1) % size
    
    elif cmd[0] == 'pop':
        if front != rear:
            print(arr[front])
            front = (front + 1) % size
        else:
            print(-1)
    
    elif cmd[0] == 'size':
        print((rear - front + size) % size)
    
    elif cmd[0] == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(arr[front])

    elif cmd[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(arr[(rear-1) % size])