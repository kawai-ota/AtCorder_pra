N = int(input())
S = list(input())
se = set()

nowx = 0
nowy = 0
se.add((nowx, nowy))
for i in range(N):

  if S[i]=="R":
    nowx +=1
  elif S[i]=="L":
    nowx -=1
  elif S[i]=="U":
    nowy += 1
  else:
    nowy -=1
  if (nowx, nowy) in se:
    print("Yes")
    exit()
  se.add((nowx, nowy))
print('No')
