# BOJ 9012 괄호 (VPS)
# 날짜: 2026-03-23
# 분류: 스택
# 핵심 아이디어:
# - '(' 나오면 push
# - ')' 나오면 pop
# - 스택 비어있는데 ')' 나오면 바로 NO
# - 마지막에 스택 비어있으면 YES
# 시간복잡도: O(n)

import sys
input = sys.stdin.readline

def val(s):
    stk = []
    for ch in s:
        if ch == '(':
            stk.append(ch)
        else:
            if not stk:
                return "NO"
            else:
                stk.pop()
    if not stk:
        return "YES"
    else:
        return "NO"
    
T = int(input())
for i in range(T):
    print(val(input().strip()))