n,k=map(int,input().split())
for _ in range(k):
    def g1(x):
        return int(''.join(sorted([*str(x)])[::-1]))
    def g2(x):
        return int(''.join(sorted([*str(x)])))
    n=g1(n)-g2(n)
print(n)