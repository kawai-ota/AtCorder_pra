s = input()
t = input()

if s == t:
  print("Yes")
else:
  for i in range(len(s) - 1):
    if s[i] != t[i]:
      if s[i + 1] == t[i] and s[i] == t[i + 1]:
        print("Yes")
        exit()
      else:
        print("No")
        exit()