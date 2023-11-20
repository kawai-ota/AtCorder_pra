n = int(input())
a = list(map(int,input().split()))
a_sort = list(set(a))
a_sort.sort()

print(a_sort[-2])