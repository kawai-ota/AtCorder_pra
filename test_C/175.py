X, K, D = map(int, input().split())

abx = abs(X)

q, r = divmod(abx, D)

if K < q:
    ans = abx - D * K
elif (K - q) % 2 == 0:
    ans = r
else:
    ans = D - r

print(ans)