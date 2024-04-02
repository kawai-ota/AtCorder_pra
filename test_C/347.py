n, a, b = map(int, input().split())
d = list(map(int, input().split()))
d = [dd % (a+b) for dd in d]
d = set(d)
d = list(d)
d.sort()
x = []
if n == 1:
    print('Yes')
    exit()
for i in range(len(d)-1):
    x.append(d[i+1]-d[i])
x.append(a+b+d[0]-d[-1])

if max(x)-1 >= b:
    print('Yes')
else:
    print('No')