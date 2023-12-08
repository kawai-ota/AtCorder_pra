n = int(input())
total = 0

for _ in range(n):
  a,b = map(int,input().split())
  total += ((a + b) * (b - a + 1) // 2)

print(total)