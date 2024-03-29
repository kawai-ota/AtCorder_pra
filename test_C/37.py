N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, N):
    a[i] += a[i-1]

ans = a[K-1]
for i in range(N-K):
    ans += a[i+K] - a[i]
print(ans)