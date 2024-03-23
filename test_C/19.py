input()
a=list(map(int,input().split()))
b=set()
for i in a:
    while i%2==0:
        i//=2
    b.add(i)
print(len(b))

