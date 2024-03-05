N = int(input())
S = [0] + list(map(int, input().split()))
T = [10**9+5] + list(map(int, input().split()))
minT = min(T)
sunuke = -1
for i in range(1, N+1):
    if T[i] == minT:
        sunuke = i

ans = [(sunuke, minT)]
while len(ans) < N:
    sunuke += 1
    if sunuke == N+1:
        sunuke = 1
    time = min(ans[-1][1]+S[ans[-1][0]], T[sunuke])
    ans.append((sunuke, time))
ans.sort(key=lambda x: x[0])
for sunuke, time in ans:
    print(time)
