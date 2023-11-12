import re
s = input()

S = set(s)

if re.search("[A-Z]",s) and re.search("[a-z]",s)and len(S) == len(s):
  print("Yes")
else:
  print("No")