S=input()
import math
kaku=set()
kouho=set()
for i in range(10):
  if S[i]=="o":
    kaku.add(i)
  elif S[i]=="?":
    kouho.add(i)
kouho=(kaku|kouho)
res=0    
for i in range(10000):
  s=str(i)
  k=s.zfill(4)
  Flag=True
  for a in list(kaku):
    if str(a) not in k:
      Flag=False
      #print(k,a)
      break
  for j in range(4):
    if int(k[j]) not in kouho:
      Flag=False
      #print(k,k,j)
      break
  if Flag:
    res+=1
print(res)
    
  
    
  
  
  