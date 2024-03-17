def cmb(n): # nC2 
    return n*(n-1)//2

s=input()
dic={}
for si in s:
    if si not in dic:
        dic[si]=0
    dic[si]+=1
ans=cmb(len(s))
isAllOne=True
for key in dic:
    ans-=cmb(dic[key])
    if dic[key]!=1:
        isAllOne=False

if not isAllOne:
    ans+=1
print(ans)