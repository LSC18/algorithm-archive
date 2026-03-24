from collections import deque
import sys

input = sys.stdin.readline

N = int(input())  # 명령어의 수 입력
que = deque()

for i in range(N):
    ord = list(input().split())  # 명령어 입력
    ord[0] = int(ord[0])  # ord[0]을 정수로 변환

    if ord[0] == 1:
        que.appendleft(ord[1])  # 앞에 추가
    elif ord[0] == 2:
        que.append(ord[1])  # 뒤에 추가
    elif ord[0] == 3:
        if que:
            print(que.popleft())  # 앞에서 삭제 후 출력
        else:
            print('-1')  # 비어 있으면 -1 출력
    elif ord[0] == 4:
        if que:
            print(que.pop())  # 뒤에서 삭제 후 출력
        else:
            print('-1')  # 비어 있으면 -1 출력
    elif ord[0] == 5:
        print(len(que))  # 큐의 길이 출력
    elif ord[0] == 6:
        if que:
            print('0')  # 큐가 비어 있지 않으면 0 출력
        else:
            print('1')  # 큐가 비어 있으면 1 출력
    elif ord[0] == 7:
        if que:
            print(que[0])  # 큐의 앞 값 출력
        else:
            print('-1')  # 큐가 비어 있으면 -1 출력
    elif ord[0] == 8:
        if que:
            print(que[-1])  # 큐의 뒤 값 출력
        else:
            print('-1')  # 큐가 비어 있으면 -1 출력
