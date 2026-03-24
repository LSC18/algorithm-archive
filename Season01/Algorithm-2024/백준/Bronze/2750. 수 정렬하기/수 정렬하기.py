n = int(input())
stk = []
for i in range(n):
    stk.append(int(input()))
num = sorted(stk)

for j in num:
    print(j)