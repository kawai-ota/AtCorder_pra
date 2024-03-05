from sys import stdin
import pprint
from itertools import *
import operator

s=input()
ch=[0]*9
ch[0]=1
mp={n:p for n,p in zip('chokudai',range(1,9))}
mod=10**9+7
for c in s:
    if c not in mp:
        continue
    ind=mp[c]
  
    ch[ind]+=ch[ind-1]
    ch[ind]%=mod
    
print(ch[8])






    

    


    
