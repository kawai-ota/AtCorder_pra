N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(10**18):
    buf = 10**18
    for j in range(N):
        if Q[j]-A[j]*i<0: break
        if B[j]==0: continue
        buf = min(buf, (Q[j]-A[j]*i)//B[j])
    else:
        ans = max(ans, buf+i)
        continue
    break

print(ans)

