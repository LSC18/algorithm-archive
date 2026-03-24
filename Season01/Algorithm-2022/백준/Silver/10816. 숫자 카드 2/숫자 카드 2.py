N = int(input())
N1 = [*map(int,input().split())]
M = int(input())
M1 = [*map(int,input().split())]
numlist = [0] * 20000001
for i in N1:
    numlist[i+10000000] += 1
for i in M1:
    print(numlist[i+10000000], end=' ')