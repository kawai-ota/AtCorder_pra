n,k = map(int,input().split())

count = 0

if n == 0:
  print(1)
else:
  while k > 0:
    n = n // k
    count +=1

print(count)