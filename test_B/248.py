a,b,k = map(int,input().split())

count = 0

while a < b:
   a = a * k
   count = count + 1

print(count)