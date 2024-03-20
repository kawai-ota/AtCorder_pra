from itertools import product

N,K=map(int,input().split())
T=[list(map(int,input().split())) for _ in range(N)]

for prod in product(range(K),repeat=N):
    tmp=0
    for i,p in enumerate(prod):
        tmp^=T[i][p]
    if tmp==0:
        print("Found")
        exit()
print("Nothing")