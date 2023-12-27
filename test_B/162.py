n = int(input())
num = 0

for i in range(1,n + 1):
   if i % 3 == 0:
     num += 0
   elif i % 5 == 0:
     num += 0
   elif i % 15 == 0:
     num += 0
   else:
     num += i

print(num)