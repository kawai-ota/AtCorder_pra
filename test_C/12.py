N = 2025 - int(input())
ans = []

for i in range(1, 10):
  for j in range(1, 10):
    if i * j == N:
      s = "{} x {}".format(i, j)
      ans.append(s)

ans.sort()

for i in range(len(ans)):
  print(ans[i])