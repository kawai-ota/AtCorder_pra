N = int(input())
comma = 0
ans = 0
L = 1
R = 10
for i in range(16):
    if(R<=N):
        ans += (R-L)*comma
    elif(L<=N and N<R):
        ans += (N-L+1)*comma
    L *= 10
    R *= 10
    if(i%3==2):
        comma += 1
print(ans)