n = int(input())
a = list(map(int,input().split()))

strings = set(a)

if len(strings) == n:
   print("Yes")
else:
   print("No")