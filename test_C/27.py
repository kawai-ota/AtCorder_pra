n=int(input())

def slv(m,turn):
    pl=0;tl=m
    while tl<=n:
        pl+=1
        tl*=2
    pr=0;tr=m
    while tr<=n:
        pr+=1
        tr=2*tr+1
    pl-=1
    pr-=1
    if pl==pr:
        return turn^((pl+1)%2)
    if slv(m*2,turn^1)==turn or slv(m*2+1,turn^1)==turn:return turn
    else:return turn^1

if slv(1,0):print("Aoki")
else:print("Takahashi")