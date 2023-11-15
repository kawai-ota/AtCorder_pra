n = int(input())

a = list(map(int,input().split()))

a[a.index(max(a))] = 0

print(a.index(max(a)) + 1)