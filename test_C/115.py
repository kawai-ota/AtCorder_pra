n, k = map(int, input().split())

h = []

for i in range(n): 
    h.append(int(input()))

h = sorted(h)

d = []

for i in range(n - k + 1): 
    d.append(h[i + k - 1] - h[i])

print(min(d))