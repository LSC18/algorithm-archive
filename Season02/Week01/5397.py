# BOJ 5397 키로거
# 날짜: 2026-03-27
# 분류: 스택, 구현
# 핵심 아이디어:
# - 커서를 기준으로 문자열을 left / right 두 스택으로 분리
# - '<' 입력 시 left → right 이동 (커서 왼쪽 이동)
# - '>' 입력 시 right → left 이동 (커서 오른쪽 이동)
# - '-' 입력 시 left pop (백스페이스)
# - 마지막에 left + reversed(right)로 결과 생성
# 시간복잡도: O(N)

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    left = []
    right = []
    s = input().strip()
    
    for ch in s:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)
    
    ans = left + right[::-1]
    
    print("".join(ans))