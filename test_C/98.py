n = int(input())
s = str(input())

dp = [0 for _ in range(n)]
dp[0] = s[1:].count('E')
for i in range(1, n):
    sa = 0
    if s[i] == 'E':
        sa -= 1
    if s[i-1] == 'W':
        sa += 1
    dp[i] = dp[i-1] + sa

ans = 10**10
for i in range(n):
    ans = min(ans, dp[i])
print(ans)