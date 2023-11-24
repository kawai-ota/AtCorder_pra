n = int(input())
a = list(map(int,input().split()))
ans = True

for i in a:
   if i % 2 == 0:
      if i % 3 == 0 and i % 5 == 0:
         continue
      else:
          ans = False

if ans:
   print("APPROVED")
else:
   print("DENIED")