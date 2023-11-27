n = int(input())

ans = False

for i in range(1,10):
   if n % i == 0 and (n // i) in [1,2,3,4,5,6,7,8,9]:
      ans = True
if ans:
   print("Yes")
else:
   print("No")