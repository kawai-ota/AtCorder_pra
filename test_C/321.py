import itertools
n=int(input())
ls=[i for i in range(1,10)]
num=[str(i) for i in range(10)]

for i in range (2,11):
    perms=list(itertools.combinations(num,i))
    for j in perms:
        lj=list(j)
        lj.sort(reverse = True)
        ls.append(int(''.join(lj)))
ls.sort()
print(ls[n-1])