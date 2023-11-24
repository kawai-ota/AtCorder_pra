a,b = map(int,input().split())

num_1 = ''
num_2 = ''

for _ in range(b):
  num_1 = num_1 + str(a)
for _ in range(a):
  num_2 = num_2 + str(b)

if a > b:
  print(num_2)
elif a < b:
  print(num_1)
else:
  print(num_1)