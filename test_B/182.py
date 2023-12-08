n = int(input())
a = list(map(int,input().split()))

ans = 0
max_cnt = 0

for i in range(2,max(a) + 1):
  cnt = 0
  for j in a:
    if j % i == 0:
       cnt += 1
  if cnt > max_cnt:
     ans = i
     max_cnt = cnt

print(ans)