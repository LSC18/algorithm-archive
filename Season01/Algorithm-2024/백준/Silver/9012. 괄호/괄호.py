import sys
input = sys.stdin.readline

n = int(input())
ans = []

for _ in range(n):
    tmp = []
    stk = input()
    val = True

    for char in stk:
        if char == '(':
            tmp.append(char)
        elif char == ')':
            if tmp: # stk에 여는 괄호가 있을 때만
                tmp.pop()
            else: # stk의 처음이 닫히는 괄호일 때
                val = False
                break
    if val and not tmp: # val == True and tmp가 비어있을 때
        ans.append('YES')
    else:
        ans.append('NO')

for k in ans:
    print(k)