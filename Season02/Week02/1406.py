# 5397 확장판
# BOJ 1406 에디터
# 날짜: 2026-03-31
# 분류: 스택, 구현
# 핵심 아이디어:
# - 커서를 기준으로 문자열을 left / right 두 스택으로 분리
# - L: left → right (커서 왼쪽 이동)
# - D: right → left (커서 오른쪽 이동)
# - B: left pop (삭제)
# - P x: left append (삽입)
# - 마지막에 left + reversed(right)로 결과 생성
# 시간복잡도: O(N + M)

import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

print("".join(left + right[::-1]))