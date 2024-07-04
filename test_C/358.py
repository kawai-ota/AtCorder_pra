n, m = map(int,input().split())
S = [input() for _ in range(n)]

Sbin = []
for s in S:
    sbin = 0
    for i in range(m):
        if s[i] == "o":
            sbin += 1 << (m - i - 1)
        else:
            sbin += 0 << (m - i - 1)
    Sbin.append(sbin)


ans = n
for bit in range(1 << n):
    x = 0
    for i in range(n):
        if (bit >> i) & 1 == 1:
            x |= Sbin[i]
    
    cnt = 0
    if x == 2**m - 1:
        cnt = bin(bit).count("1")
        if cnt < ans:
            ans = cnt
print(ans)