n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_b = min(b)
max_a = max(a)

result = max(0, min_b - max_a + 1)

print(result)