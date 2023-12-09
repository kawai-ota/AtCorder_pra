s = input()
oxx = 'oxx' * 30
for i in range(len(oxx)):
  if oxx[i:i+len(s)] == s:
    print("Yes")
    exit(0)
print("No")