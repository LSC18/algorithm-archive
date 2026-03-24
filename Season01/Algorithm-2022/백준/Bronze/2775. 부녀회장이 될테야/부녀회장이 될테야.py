T = int(input())
answer = 0
for i in range(T):
    k = int(input())
    n = int(input())
    f0 = list(range(1,n+1))

    for j in range(k):
        for l in range(1,n):
            f0[l] += f0[l-1]
    print(f0[-1])