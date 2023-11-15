a = input()
b = input()
c = input()
d = input()
e = [a,b,c,d]
f = set(e)

keys = ['H','2B','3B','HR']

if len(f) == len(keys):
  print("Yes")
else:
  print("No")