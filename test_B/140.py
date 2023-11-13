n = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

s = 0

for i in range(n):
   s = s + b[a[i] - 1]
   if i != n - 1 and a[i] + 1 == a[i + 1]:
      s = s + c[a[i] - 1]

print(s)