n = int(input())
l = list(map(int,input().split()))
d = {}
for i in l:
  d.setdefault(i,0)
  d[i] += 1
cnt = 0
for k,v in d.items():
  if k <= v:
    cnt += v - k
  else:
    cnt += v
print(cnt)