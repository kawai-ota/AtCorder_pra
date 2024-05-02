from itertools import product
n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]
m = 10000
for Q in product(range(4), repeat=n):
  A, B, C = [], [], []
  for i in range(n):
    if Q[i] == 1:
      A.append(L[i])
    elif Q[i] == 2:
      B.append(L[i])
    elif Q[i] == 3:
      C.append(L[i])
  if 0 < len(A) <= a and 0 < len(B) <= b and 0 < len(C) <= c:
    s = 10*(len(A)+len(B)+len(C)-3)+abs(sum(A)-a)+abs(sum(B)-b)+abs(sum(C)-c)
    m = min(m, s)
print(m)