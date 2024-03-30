N = int(input())
a = [[i, 0] for i in range(N + 1)]
i = 1
for tall in map(int, input().split()):
  a[i][1] = tall
  i += 1
  
a.sort(key = lambda x: x[1], reverse = True)
for i in range(N):
  print(a[i][0])