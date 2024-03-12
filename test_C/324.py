import sys
sys.setrecursionlimit(10**8)



N,T = input().split()
N = int(N)

ans = []
for k in range(N):
  S = list(input())
  ok = True
  if len(S) == len(T):
    if S == T:
      pass
    else:
      n = 0
      for i in range(len(T)):
        if S[i] == T[i]:
          pass
        else:
          if n == 0:
            n += 1
          else:
            ok = False
            break
  elif len(S)+1 == len(T):
    n = 0
    i = 0
    for j in range(len(T)):
      if i < len(S) and S[i] == T[j]:
        i += 1
      else:
        if n == 0:
          n += 1
        else:
          ok = False
          break
  elif len(S)-1 == len(T):
    n = 0
    i = 0
    for j in range(len(S)):
      if i < len(T) and S[j] == T[i]:
        i += 1
      else:
        if n == 0:
          n += 1
        else:
          ok = False
          break
  else:
    ok = False

  if ok:
    ans.append(k+1)

ans.sort()
print(len(ans))
print(*ans)
