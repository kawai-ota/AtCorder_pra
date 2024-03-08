n,k=map(int,input().split())
a=list(map(int,input().split()))
a_set=set(sorted(a))
for i in range(k):
    if i not in a_set:
        print(i)
        exit()
print(k)