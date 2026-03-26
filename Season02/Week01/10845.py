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