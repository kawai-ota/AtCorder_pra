N,K=list(map(int, input().split()))
s=input()
S=list(s)
iS=sorted(S)
SS=S[:]
if K<=1:
    print("".join(S))
    exit()

alf=[set() for _ in range(30)]

for i in range(N):
    alf[ord(S[i])-97].add(i)

cnt=[0]*30
for i in range(30):
    cnt[i]=len(alf[i])

def check(num):
    c=0
    ccnt=cnt[:]
    cccnt=cnt[:]
    tans=ans+chr(num+97)
    for j in range(len(tans)):
        if tans[j]!=S[j]:
            c+=1
            ccnt[ord(tans[j])-97]-=1
            cccnt[ord(S[j])-97]-=1
    for j in range(30):
        c+=ccnt[j]-min(ccnt[j],cccnt[j])
    if c<=K:
        return True
    else:
        return False

ans = ""
for i in range(N):
    for j in range(27):
        if cnt[j] and check(j):
            ans+=chr(j+97)
            cnt[j]-=1
            break
print(ans)
