N,Q = map(int,input().split())
S = input()

conti=[]
for i in range(N-1):
    if ord(S[i])==ord(S[i+1]):
        conti.append(1)
    else:
        conti.append(0)

result = [0]
for i in range(1,N):
    result.append(result[i-1]+conti[i-1])

for _ in range(Q):
    l,r= map(int,input().split())
    print(result[r-1]-result[l-1])

