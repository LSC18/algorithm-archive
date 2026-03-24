N, K = map(int, input().split())
Nf = 1
N_K = 1
Kf = 1
for i in range(1, N+1):
    Nf *= i
for j in range(1, N-K+1):
    N_K *= j
for k in range(1, K+1):
    Kf *= k
answer = Nf // (N_K * Kf)
print(answer)