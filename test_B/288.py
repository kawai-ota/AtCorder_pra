n,k = map(int,input().split())
s = [input() for _ in range(n)]

s = s[:k]
s.sort()

for i in range(k):
  print(s[i])