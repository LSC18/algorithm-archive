import sys
input = sys.stdin.readline

N = int(input())
stk = []
out = []
i = 1

for _ in range(N):
    cmd = int(input())

    while i <= cmd:
        stk.append(i)
        out.append('+')
        i += 1

    if stk and stk[-1] == cmd:
        stk.pop()
        out.append('-')
    else:
        print("NO")
        sys.exit()

for x in out:
    print(x)