from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tar = list(map(int, input().split()))
dq = deque(range(1,n+1))
cnt = 0

for t in tar:
    while True:
        if dq[0] == t:
            dq.popleft()
            break # dq의 처음과 타겟이 일치하면 뽑고 멈추기
        else:
            if dq.index(t) < len(dq)/2: # 왼쪽으로 회전시켜야 하는 경우
                # t < len(dq)/2가 아닌 이유는 초기값 외에 t와 dq.index(t)가 같지 않을 수 있기 때문
                # dq.index(t) < n/2가 아닌 이유도 동일.
                while dq[0] != t: # dq의 첫번째 인덱스가 t랑 같아질 때까지 반복
                    dq.append(dq.popleft())
                    cnt += 1
            else: # 오른쪽으로 회전시켜야 하는 경우
                while dq[0] != t:
                    dq.appendleft(dq.pop())
                    cnt += 1
print(cnt)