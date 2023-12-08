n = int(input())
h = list(map(int,input().split()))
ans = 0

for i in h:
  if ans < i:
    ans = i
  elif ans == i:
    print(ans)
    exit()
  elif ans > i:
    print(ans)
    exit()
    
print(ans)    