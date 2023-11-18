n = int(input())
a = list(map(int,input().split()))
a.sort()

for i in range(n):
  if a[i + 1] != a[i] + 1:
     print(a[i] + 1)
     exit()
print(a[-1] + 1)