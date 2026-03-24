N = int(input())
num = 1
stk = 1
while N > num:
    num += 6*stk
    stk += 1
print(stk)