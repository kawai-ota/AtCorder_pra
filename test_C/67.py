N = int(input())
A = list(map(int,input().split()))
sunu = A[0]
arai = sum(A[1:N])
M = abs(arai-sunu)
for a in range(1,N-1):
    sunu += A[a]
    arai -= A[a]
    if abs(arai-sunu) <= M:
        M = abs(arai-sunu)
print(M)