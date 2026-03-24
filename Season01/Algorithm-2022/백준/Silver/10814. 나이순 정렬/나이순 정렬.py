N = int(input())
lst = []
for i in range(N):
    a, n = map(str ,input().split(' '))
    a = int(a)
    lst.append((a,n))
lst.sort(key=lambda x: x[0])

for i in lst:
    print(i[0],i[1])