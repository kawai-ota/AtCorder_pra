n = int(input())
rg = 1000001
c = [0] * rg

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

for x in a:
    c[x] += x
for i in range(1, rg):
    c[i] += c[i - 1]

for x in a:
    print(c[rg - 1] - c[x], end = ' ')