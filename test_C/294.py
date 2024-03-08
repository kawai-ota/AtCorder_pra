N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

i,j=0,0
ans_A,ans_B=[],[]
for k in range(1,N+M+1):
    if j==M or (i<N and A[i]<B[j]):
        ans_A.append(k); i+=1
    else:
        ans_B.append(k); j+=1
print(*ans_A)
print(*ans_B)