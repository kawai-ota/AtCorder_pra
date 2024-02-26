n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sm = 0
i = 0
while i < n and sm + a[i] <= k:
    sm += a[i]
    i += 1
a_max = i

j = 0
while j < m and sm + b[j] <= k:
    sm += b[j]
    j += 1

ans = i + j
for i in range(a_max-1, -1, -1):
    sm -= a[i]
    while j < m and sm + b[j] <= k:
        sm += b[j]
        j += 1
    ans = max(ans, i + j)
print(ans)