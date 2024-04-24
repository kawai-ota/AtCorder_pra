N = int(input())
S = []
ans = ""
if N != 0:
  while N != 1:
    add = abs(N % (-2))
    S.append(add)
    N = int((N-add) / (-2))
  else:
    S.append(1)
else :
  print(0)
  exit()

for i in range(len(S)): ans += str(S[len(S)-i-1])
print(ans)