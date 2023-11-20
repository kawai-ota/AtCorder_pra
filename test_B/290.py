n,k = map(int,input().split())
s = input()
strings = ''
count = 0

for i in range(n):
  if count >= k:
      strings += 'x'
  elif count < 0 and s[i] == 'o':
      strings += 'o'
      count += 1
  else:
      strings += s[i]

print(strings)