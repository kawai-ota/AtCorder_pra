S=list(input())
K=int(input())
n=0
while n!=K:
 if S[n]!="1":
  print(S[n])
  break
 n+=1
else:
  print(1)