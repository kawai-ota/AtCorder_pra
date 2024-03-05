N = int(input())
ans = N*(N-1)//2
S = []
for i in range(N):
  t,l,r = map(int,input().split())
  for tt,ll,rr in S:
    f = 0
    if rr < l:
      f = 1
    if r < ll:
      f = 1
    if rr == l:
      if (tt % 2 == 0) or (t >= 3):
        f = 1
    if r == ll:
      if (t % 2 == 0) or (tt >= 3):
        f = 1
    ans -= f
  S.append((t,l,r))
print(ans)