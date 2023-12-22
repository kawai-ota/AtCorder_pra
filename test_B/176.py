s = input()
total = 0

for i in s:
  total += int(i)

if total % 9 == 0:
   print("Yes")
else:
   print("No")