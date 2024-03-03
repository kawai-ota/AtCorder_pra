from collections import defaultdict

n=int(input())
A=list(map(int,input().split()))
B=[]
for i in range(n):
    B.append(A[i]%200)
dic=defaultdict(int)
for b in B:
    dic[b]+=1
dic2=list(dic.items())
def comb(n):
    return n*(n-1)//2
ans=0
for i in dic2:
    ans+=comb(i[1])
print(ans)
