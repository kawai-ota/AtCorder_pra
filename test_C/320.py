from itertools import permutations
M=int(input())
S=[]

for _ in range(3):
  s=input()
  S.append(s+s)

def solve(p,d):
  if any(d not in S[i] for i in range(3)): return 10**9
  crr=0
  for i in range(3):
    crr+=S[p[i]][crr%M:].index(d)+1
  return crr-1

ans=10**9
for d in range(10):
  for p in permutations(range(3)):
    ans=min(ans,solve(p,str(d)))

print(ans if ans!=10**9 else -1)