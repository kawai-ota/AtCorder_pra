n = int(input())
f = []
p = []
for i in range(n):
  f.append(list(map(int,input().split())))
for i in range(n):
  p.append(list(map(int,input().split())))

ans = -10**18

for i in range(1,1<<10):
  profit = 0
  joisino = [0]*10
  for j in range(10):
    open = (i>>j)%2
    joisino[j] = open
 
  for j in range(n):
    cn = 0
    for k in range(10):
      cn += f[j][k] and joisino[k]
    profit += p[j][cn]
  
  ans = max(ans,profit)

print(ans)