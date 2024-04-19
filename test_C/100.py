n = int(input())
a = tuple(map(int, input().split()))
m = sum((ai & -ai).bit_length() - 1 for ai in a)
print(m)

