N,K = map(int, input().split())
c = list(map(int, input().split()))
from collections import defaultdict
cnt = defaultdict(int)
s = 0
for i in range(K):
    if cnt[c[i]] == 0:
        s += 1
    cnt[c[i]] += 1

ans = s
for i in range(N-K):
    if cnt[c[i+K]] == 0:
        s+=1
    cnt[c[i+K]]+=1

    if cnt[c[i]] == 1:
        s-=1
    cnt[c[i]]-=1
    ans = max(ans,s)
print(ans)



