N = int(input())
from collections import Counter
cnt_even = Counter()
cnt_odd = Counter()

ce = 0
co = 0

V = list(map(int, input().split()))
for i in range(N):
  if i % 2 == 0:
    cnt_even[V[i]] += 1
    ce += 1
  else:
    cnt_odd[V[i]] += 1
    co += 1

if len(set(V)) == 1:
  print(N//2)
  exit()
  
even = cnt_even.most_common()
odd = cnt_odd.most_common()

ans = 1<<60
for i in range(2):
  if i >= len(even):
    break
  for j in range(2):
    if j >= len(odd):
      break
    if even[i][0] == odd[j][0]:
      continue
    ans = min(ans, ce - even[i][1] + co - odd[j][1])
print(ans)