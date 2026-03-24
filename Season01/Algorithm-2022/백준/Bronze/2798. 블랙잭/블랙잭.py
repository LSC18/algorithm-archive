# 블랙잭 = 카드 합 21 under에서 max 값
N, M =  map(int,input().split())
stack = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if stack[i] + stack[j] + stack[k] > M:
                continue
# 3개의 랜덤한 값을 모두 비교해여하므로 3중 for문
            else:
                ans = max(ans, stack[i] + stack[j] + stack[k])
print(ans)