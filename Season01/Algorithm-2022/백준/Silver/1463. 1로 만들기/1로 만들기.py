dp = [-1] * 1000001

def f(n):
    if dp[n] != -1:
        return dp[n]
    if n == 1:
        return 0
    dp[n] = 1e9
    if n % 3 == 0:
        dp[n] = f(n // 3) + 1
    if n % 2 == 0:
        dp[n] = min(dp[n], f(n // 2) + 1)
    dp[n] = min(dp[n], f(n - 1) + 1)
    return dp[n]
for i in range(1, 1000001):
    f(i)

X = int(input())
print(f(X))
