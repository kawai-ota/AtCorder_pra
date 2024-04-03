n,m=map(int,input().split())
count=0
if n*2<=m:
    count+=n
    m-=n*2
    count+=m//4
else:
    count+=m//2
print(count)