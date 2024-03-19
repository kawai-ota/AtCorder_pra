N=int(input())
P=[*'123456']
for n in range(N%30):
    i=n%5
    P[i],P[i+1]=P[i+1],P[i]
R=''.join(P)
print(R)