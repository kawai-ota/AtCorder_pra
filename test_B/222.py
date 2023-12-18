n,p = map(int,input().split())
a = list(map(int,input().split()))
count = 0

for i in a:
  if i < p:
    count += 1
    
print(count)