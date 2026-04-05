# BOJ 1874 스택 수열
# 날짜: 2026-04-03
# 분류: 스택, 시뮬레이션
# 핵심 아이디어:
# - 1부터 N까지 숫자를 순서대로 스택에 push
# - 목표 수열의 값(cmd)이 나올 때까지 push 진행
# - 스택 top이 cmd와 같으면 pop
# - 다르면 해당 수열은 만들 수 없으므로 "NO"
# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

N = int(input())
stk = []
out = []
i = 1  # 다음에 push할 숫자

for _ in range(N):
    cmd = int(input())

    # cmd까지 push
    while i <= cmd:
        stk.append(i)
        out.append('+')
        i += 1

    # 스택 top이 원하는 값이면 pop
    if stk and stk[-1] == cmd:
        stk.pop()
        out.append('-')
    else:
        print("NO")
        sys.exit()

for x in out:
    print(x)