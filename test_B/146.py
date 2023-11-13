s = input()
n = int(input())

for char in s:
  print((chr(ord(char) + n - ord("A")) % 26 + ord("A")),end = '')

print("")