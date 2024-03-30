N = int(input())
A = list(map(int,input().split()))
cnt = [0]*N

for i in range(N):
    cnt[A[i]] += 1


if N%2==0:
    flag = True
    for i in range(N):
        if i%2==0:
            if cnt[i] !=0:
                flag = False
        else:
            if cnt[i]!=2:
                flag = False
else:
    flag = True
    for i in range(N):
        if i==0:
            if cnt[i] !=1:
                flag = False
            continue

        if i%2==1:
            if cnt[i] !=0:
                flag = False
        else:
            if cnt[i]!=2:
                flag = False
if flag:
    mod = 10**9+7
    ans = 1
    for i in range(N//2):
        ans *= 2
        ans %=mod
    print(ans)
else:
    print(0)
