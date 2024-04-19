N = int(input())
dp = [10**10]*(N+1)
def rec(t,l):
    n = 1
    while t > n:
        n *= l
        if n*l > t:
            break
    return n
for i in range(N+1):
    if i <= 5:
        dp[i] = i
    else:
        dp[i] = 1 + dp[i-rec(i,6)]
        dp[i] = min(dp[i], 1 + dp[i-rec(i,9)])
print(dp[-1])