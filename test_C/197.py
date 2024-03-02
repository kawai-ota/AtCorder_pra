n=int(input())
a=list(map(int,input().split()))
ans=float("inf")
for bit in range(1<<n-1):
    xor=0
    oor=0
    for shift in range(n):
        oor|=a[shift]
        if bit>>shift&1 or shift==n-1:
            xor^=oor
            oor=0
    ans=min(xor,ans)
print(ans)