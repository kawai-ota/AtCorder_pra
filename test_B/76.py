n = int(input())
k = int(input())
ans = 1

for _ in range(n):
  if ans * 2 <= ans + k:
     ans = ans * 2
  elif ans * 2 > ans + k:
     ans = ans + k

print(ans)