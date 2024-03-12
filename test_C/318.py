N,D,P=map(int,input().split())
F=list(map(int,input().split()))
F=sorted(F)
SF=sum(F)
ans=SF
X=N//D

for x in range(X):
    for d in range(D):
        SF=SF-F.pop()
    if ans>SF+P*(x+1):
        ans=(SF+P*(x+1))
    else:
        break
ans=min(ans,P*(X+1))
print(ans)