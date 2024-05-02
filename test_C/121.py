n, m = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

ab = sorted(ab)

la = []
lb = []

for i in range(n):
    la.append(ab[i][0])
    lb.append(ab[i][1])

bought = 0
ans = 0
i = 0

while bought < m:
    bought += 1
    ans += la[i]
    lb[i] -= 1

    if lb[i] == 0:
        i += 1

print(ans)


