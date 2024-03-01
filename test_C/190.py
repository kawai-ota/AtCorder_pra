N,M=map(int,input().split())
T=[list(map(int,input().split())) for i in range(M)]
K=int(input())
L=[list(map(int,input().split())) for i in range(K)]
ans=0

for msk in range(1<<K):
    cnt=[False]*(N+1)
    for i in range(K):
        c,d=L[i]
        if msk>>i&1:
            cnt[d]=True
        else:
            cnt[c]=True
    res=0
    for i in range(M):
        a,b=T[i]
        if cnt[a] and cnt[b]:
            res+=1
    ans=max(ans,res)
print(ans)