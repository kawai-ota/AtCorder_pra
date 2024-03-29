N = int(input())
A = [int(x) for x in input().split()]

INF = float("INF")

cuts = []
l = 0
while l < N:
   r = l
   tail = -INF
   while r < N and tail < A[r]:
      tail = A[r]
      r += 1
   cuts.append((l, r))
   l = r

ans = 0
for l, r in cuts:
   n = r-l
   ans += n*(n+1) // 2

print(ans)
