N=int(input())
S=input()
lis=list(S)
Q=int(input())
r=0
for i in range(Q):
    t,a,b=map(int,input().split())
    a-=1
    b-=1
    if t==1:
        if r:
            if a>=N:
                ind1=a-N
            else:
                ind1=a+N
            if b>=N:
                ind2=b-N
            else:
                ind2=b+N
        else:
            ind1=a
            ind2=b
        lis[ind1],lis[ind2]=lis[ind2],lis[ind1]
    else:
        r=1-r
if r:
    print("".join(lis[N:])+"".join(lis[:N]))
else:
    print("".join(lis))
            
                