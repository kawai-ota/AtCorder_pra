n = int(input())

key = str(n)
sum = 0

for i in range(len(key)):
  sum += int(key[i])

if n % sum == 0:
  print("Yes")
else:
  print("No")