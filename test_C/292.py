N = int(input())

f = [0]*(N+1)
for a in range(N):
    for b in range(N):
        if a*b > N: break
        f[a*b] += 1

ans = 0
for x in range(1,N):
    ans += f[x] * f[N-x]

print(ans)