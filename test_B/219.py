a = input()
b = input()
c = input()
t = input()

key = len(t)
strings = ''

for i in range(key):
  if t[i] == '1':
    strings = strings + a
  elif t[i] == '2':
    strings = strings + b
  elif t[i] == '3':
    strings = strings + c
    
print(strings)    