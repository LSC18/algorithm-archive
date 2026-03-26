# BOJ 10866 덱
# 날짜: 2026-03-24
# 분류: 덱, 구현
# 핵심 아이디어:
# - 배열 기반 원형 큐로 덱 구현
# - front, rear 포인터 관리
# - push_front / push_back 양방향 처리
# - 인덱스는 mod 연산으로 순환
# 시간복잡도: O(1)

import sys
input = sys.stdin.readline

T = int(input())
size = 2*T
arr = [0]*size
front = rear = size // 2

for i in range(T):
    tmp = input().split()
    
    if tmp[0] == 'push_front':
        front = (front - 1) % size
        arr[front] = tmp[1]
    elif tmp[0] == 'push_back':
        arr[rear] = tmp[1]
        rear = (rear + 1) % size

    elif tmp[0] == 'pop_front':
        if front != rear:
            print(arr[front])
            front = (front + 1) % size
        else:
            print(-1)
    elif tmp[0] == 'pop_back':
        if front != rear:
            rear = (rear - 1) % size
            print(arr[rear])
        else:
            print(-1)
    
    elif tmp[0] == 'size':
        print((rear - front + size) % size)
    elif tmp[0] == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    
    elif tmp[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(arr[front])
    elif tmp[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(arr[(rear-1) % size])