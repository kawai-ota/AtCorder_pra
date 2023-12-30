k = int(input())
s = input()
result = ''

if len(s) > k:
  s = s[:k]
  result = s + '...'
else:
  print(s)