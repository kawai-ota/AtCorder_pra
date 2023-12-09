a,b = input().split()
l = min(len(a),len(b))

for i in range(l):
  c,d = int(a[len(a) - 1 - i]),int(b[len(b) - 1 - i])
  if c + d > 9:
     print("Hard")
     exit()
print("Easy")