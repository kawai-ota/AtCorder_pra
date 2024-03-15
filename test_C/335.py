from collections import Counter

n , q = map(int,input().split())

dic = Counter()
x = 1
y = 0
dic[0] = (x , y)
time = 0

for i in range(q) :
  line = input().split()
  if line[0] == '1' :
    c = line[1]
    if c == 'R' :
      x += 1
    elif c == 'L' :
      x -= 1
    elif c == 'U' :
      y += 1
    else :
      y -= 1
    time += 1
    dic[time] = (x , y)
  else :
    p = int(line[1])
    dist = (p - 1)
    if time - dist < 0 :
      print(p - time , 0)
    else :
      print(*dic[(time - dist)])