N = int(input())
x = 10**9+7

def sieve(N):
  L = list(range(N+1))
  for i in range(2*2, len(L), 2):
    L[i] = 0
  n = 3
  while n*n <= N:
    if L[n] != 0:
      for i in range(2*n, len(L), n):
        L[i] = 0
    n += 2
  return sorted(list(set(L))[2:])

L = sieve(N)
D = {l:0 for l in L}
for i in range(2, N+1):
  n = i
  if i in D:
    D[n] += 1
    continue
  else:
    for l in L:
      while n%l == 0:
        D[l] += 1
        n //= l
      if n == 1:
        break

ans = 1
for d in D:
  ans *= D[d]+1
  ans %= x
print(ans)