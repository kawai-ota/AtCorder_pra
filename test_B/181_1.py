n = int(input())
total = 0

for _ in range(n):
  a,b = map(int,input().split())
  for num in range(a,b + 1):
     total += num

print(total)