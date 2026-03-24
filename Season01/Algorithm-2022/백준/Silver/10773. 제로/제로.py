K = int(input())
stk = []
for i in range(K):
    N = int(input())
    if N == 0:
        stk.pop()
    else:
        stk.append(N)
print(sum(stk))