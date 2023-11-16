n = int(input())
price = 0
day = 0

for i in range(10 ** 9):
   price += (i + 1)
   day += 1
   if price >= n:
     print(day)
     exit()