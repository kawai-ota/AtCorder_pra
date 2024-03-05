h, w, n = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())


aa = {e: i for i, e in enumerate(sorted(set(a)))}
bb = {e: i for i, e in enumerate(sorted(set(b)))}

for i in range(n):
    print(aa[a[i]] + 1, bb[b[i]] + 1)
