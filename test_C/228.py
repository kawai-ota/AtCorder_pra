N,K=map(int,input().split())
lis=[]
for _ in range(N):
    p1,p2,p3=map(int,input().split())
    lis.append(p1+p2+p3)
lis2=lis[::]
lis2.sort(reverse=True)
for i in range(N):
    if lis[i]+300>=lis2[K-1]:
        print('Yes')
    else:
        print('No')