n = int(input())
P = list(map(int,input().split()))

memo = [-1] * (n + 1)

for i in range(n) :
  memo[P[i]] = i + 1
  
print(*memo[1 :])