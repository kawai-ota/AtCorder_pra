n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if a[i]>x:
        ans += (a[i]-x)
        a[i] -= (a[i]-x)
    if a[i]+a[i+1]>x:
        ans += (a[i]+a[i+1]-x)
        a[i+1] -= (a[i]+a[i+1]-x)

print(ans)
            