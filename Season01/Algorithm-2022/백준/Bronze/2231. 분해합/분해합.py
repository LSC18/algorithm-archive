N = int(input())
ans = 0
for i in range(1,N+1):
    a = list(map(int,str(i)))
    ans = i + sum(a)
    if ans == N:
        print(i)
        break
    if i == N:
        print(0)