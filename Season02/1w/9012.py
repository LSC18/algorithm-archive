# import sys
# input = sys.stdin.readline

# # paranthesis String = PS
# # Valid PS = VPS
# T = int(input())
# for i in range(T):
#     s = input().strip()
#     stk = []
#     vps = True
    
#     for ch in s:
#         if ch == '(':
#             stk.append(ch)
#         elif ch == ')':
#             if len(stk) == 0:
#                 print("NO")
#                 break
#             stk.pop()
#     else:
#         if not stk:
#             print("YES")
#         else:
#             print("NO")

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