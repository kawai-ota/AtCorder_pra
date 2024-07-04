N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

#initialize lis
lis = []
for i in range(N):
    lis.append(0)


for i in range(N):
    lis[A[i-1]-1] = max(lis[A[i-1]-1], W[i-1])
print(sum(W) - sum(lis))
