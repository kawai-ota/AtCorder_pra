N,M = map(int,input().split())
INF = -10**10
G = [[INF]*N for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    G[a][b] = c
    G[b][a] = c

dp = [[INF] * (1<<N) for _ in range(N)]

for i in range(N):
    dp[i][1<<i] = 0

for bit in range(1<<(N)):
    for j in range(N):
        for k in range(N):
            if  (not (bit >> k) & 1) and ((bit >> j) & 1):
                dp[k][bit|(1<<k)] = max(dp[j][bit] + G[j][k],dp[k][bit|(1<<k)])
 
ans = max([max(dp[i]) for i in range(N)])
print(ans)