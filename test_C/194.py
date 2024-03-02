N = int(input())
A = list(map(int,input().split()))

rui1 = []
rui2 = []
su1 = 0
su2 = 0
for i in range(N):
    su1 += A[i]**2
    su2 += A[i]

    rui1.append(su1)
    rui2.append(su2)

#print(rui1,rui2)
ans = 0
for i in range(N):
    ans += (A[i]**2)*(N-(i+1)) - (rui2[N-1]-rui2[i])*2*A[i] +(rui1[N-1]-rui1[i])
    #print(ans, (A[i]**2)*(N-(i+1)),(rui2[N-1]-rui2[i])*2*A[i])

print(ans)