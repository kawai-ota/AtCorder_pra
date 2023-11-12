n = int(input())
a = set(map(int,input().split()))

for i in range(n + 1):
  if i not in a:
     print(i)
     exit(i)