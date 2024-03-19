N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())
dp = [100000]*301
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
if N == NG1 or N == NG2 or N == NG3:
	print('NO')
	exit()
for i in range(4, 301):
	if i != NG1 and i != NG2 and i != NG3:
		dp[i] = min(dp[i-1]+1, dp[i-2]+1, dp[i-3]+1)
if dp[N] <= 100:
	print('YES')
else:
	print('NO')