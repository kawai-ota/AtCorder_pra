n = int(input())
h = [0]+list(map(int,input().split()))
ans = 0

for i in range(1,n+1):
    ans += max(h[i]-h[i-1],0)

print(ans)