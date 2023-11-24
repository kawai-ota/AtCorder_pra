n = int(input())
s = input()
ans = False

if len(s) % 2 == 0:
  mid = len(s) // 2
  word_1 = s[:mid]
  word_2 = s[mid:]
  if word_1 == word_2:
     ans = True

if ans:
  print("Yes")
else:
  print("No")