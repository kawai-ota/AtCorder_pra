n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]

time=0
for a,b in ab:
    time+=a/b
time/=2

length=0
for i in range(n):
    a,b=ab[i]
    
    if time-a/b>=0:
        length+=a
        time-=a/b
    else:
        length+=time*b
        break

print(length)