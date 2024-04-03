from collections import Counter

n = int(input())
counter = Counter(input())

for _ in range(n - 1):
  counter &= Counter(input())

ans = ""

for char, cnt in sorted(counter.items()):
  ans += char * cnt
  
print(ans)