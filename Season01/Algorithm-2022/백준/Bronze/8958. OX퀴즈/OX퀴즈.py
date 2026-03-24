n = int(input())
for i in range(n):
    s = input()
    a = 0
    b = 0
    for j in s:
        if j == 'O':
            a += 1
            b+=a
        else:
            a = 0
    print(b)