n=int(input())
fs = [list(map(int,input().split())) for _ in range(n)]

fs = sorted(fs, key=lambda x: x[1],reverse=True)

s=fs[0][1]
f=fs[0][0]
ans=0
for i in range(1,n):
    if fs[i][0] ==f:
        ans=max(ans,s+fs[i][1]//2)
    if fs[i][0] !=f:
        ans=max(ans,s+fs[i][1])

print(ans)



