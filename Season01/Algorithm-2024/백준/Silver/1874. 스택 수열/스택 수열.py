import sys
input = sys.stdin.readline

n = int(input()) # 수열의 길이
seq = [int(input()) for _ in range(n)] # 주어진 수열 [4,3,6,8,7,5,2,1]
stk = [] # 스택
cnt = 1 # 현재 넣을 수
rst = [] # 결과물

for num in seq:
    # 현재 넣을 수가 목표 수보다 작거나 같으면 계속 push
    while cnt <= num:
        stk.append(cnt)
        rst.append('+')
        cnt += 1
    if stk[-1] == num:
        stk.pop()
        rst.append('-')
    else:
        print('NO')
        exit()
print('\n'.join(rst))