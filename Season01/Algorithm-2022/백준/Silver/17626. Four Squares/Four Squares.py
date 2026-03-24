def solution(n):
    answer = 1e9

    square_set = set()
    for d in range(0, 225):
        square_set.add(d*d)

    for a in range(0, 225):
        if a*a > n:
            break
        for b in range(a, 225):
            if a*a + b*b > n:
                break
            for c in range(b, 225):
                if a*a + b*b + c*c > n:
                    break

                if n - (a*a + b*b + c*c) in square_set:
                    d = n - (a*a + b*b + c*c)
                    answer = min(answer, (a!=0) + (b!=0) + (c!=0) + (d!=0))
    return answer
n = int(input())
print(solution(n))