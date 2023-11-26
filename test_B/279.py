s = input()
t = input()

if t == s:
  print("Yes")
elif len(s) < len(t):
  print("No")
else:
  for i in range(len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
      print("Yes")
      break
  else:
    print("No")