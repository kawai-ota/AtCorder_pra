N, Q = map(int, input().split())

lis = [0] * (N + 1)
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    lis[l] += 1
    lis[r + 1] -= 1

ans = []
for i in range(N):
    ans.append(lis[i] % 2)
    lis[i + 1] += lis[i]

print(*ans, sep='')
