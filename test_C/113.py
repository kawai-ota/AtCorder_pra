N, M = map(int, input().split())
r = [None] * M
c = [1] * (N + 1)
l = []
for i in range(M):
    p, y = map(int, input().split())
    l.append((y, i, p))
l.sort()
for y, i, p in l:
    r[i] = f"{p:06}{c[p]:06}"
    c[p] += 1
for x in r:
    print(x)
