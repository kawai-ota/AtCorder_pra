n = int(input())
s = list(input().split())

s_set = set(s)

if len(s_set) == 4:
    print("Four")
else:
    print("Three")