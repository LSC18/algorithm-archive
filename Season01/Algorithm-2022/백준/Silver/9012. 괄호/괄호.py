T = int(input())

for i in range(T):
    stk = 0
    K = list(input())
    for j in K:
        if j == '(':
            stk += 1
        elif j == ')':
            stk -= 1
        if stk < 0:
            print('NO')
            break
    if stk > 0:
        print('NO')
    elif stk == 0:
        print('YES')
