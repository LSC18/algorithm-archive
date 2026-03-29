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