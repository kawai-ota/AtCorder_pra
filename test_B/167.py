a,b,c,k = map(int,input().split())

count = 0

if a >= k:
  print(k)
elif k <= a + b:
  print(a)
else:
  print(a - (k - a - b))