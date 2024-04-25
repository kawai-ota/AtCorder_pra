n = int(input())
info = [list(map(int, input().split())) for i in range(n)]
for px in range(101):
  for py in range(101):
    height = -1
    for i in range(n):
      x,y,h = info[i]
      if h > 0:
        height = h + abs(px - x) + abs(py - y)
        break
    for i in range(n):
      x,y,h = info[i]
      if h != max(height - abs(px - x) - abs(py - y), 0):
        break
    else:
      print(px, py, height)
      exit()
print(-1)