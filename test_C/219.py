X = input()
N = int(input())
S = [['',input()] for _ in range(N)]

D = dict()
for i,x in enumerate(X):
    D[x]=chr(97+i)

for s in S:
    for t in s[1]:
        s[0]+=D[t]

S.sort()

for s in S:
    print(s[1])
