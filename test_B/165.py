x = int(input())
num = 100
count = 0

while True:
  count = count + 1
  num = num + (num // 100)

  if num >= x:
    break

print(count)