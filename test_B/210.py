n = int(input())
s = input()

for i in range(n):
  if str(s[i]) == 1 and i % 2 == 0:
      print("Takahashi")
      break
  elif str(s[i]) == 1 and i % 2 != 0:
      print("Aoki")
      break