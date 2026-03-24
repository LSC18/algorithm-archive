T = int(input())
def go(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return go(n-1) + go(n-2) + go(n-3)

for i in range(T):
    n = int(input())
    print(go(n))