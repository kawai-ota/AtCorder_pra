from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

ans = 10 ** 100
for i in range(n):
    idx = bisect_left(b, a[i])
    if idx >= 0 and idx < m:
        ans = min(ans, abs(a[i] - b[idx]))
    if idx + 1 < m:
        ans = min(ans, abs(a[i] - b[idx + 1]))
    if idx - 1 >= 0:
        ans = min(ans, abs(a[i] - b[idx - 1]))

print(ans)