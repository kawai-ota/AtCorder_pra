N = int(input())
imos = [0] * (1 << 20)
for _ in range(N):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[b + 1] -= 1
for i in range(10**6):
    imos[i + 1] += imos[i]
print(max(imos))