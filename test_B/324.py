n = int(input())

for i in range(n + 1):
   if 2 ** i > n:
      break
   for j in range(n + 1):
      if (2 ** i) * (3 ** i) > n or 3 ** j > n:
        break
      elif (2 ** i) * (3 ** i) == n:
        print("Yes")
print("No")