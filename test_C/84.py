N = int(input())
C = list()
S = list()
F = list()

for i in range(N-1):
    c,s,f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)
for i in range(N):
    time = 0
    if i == N-1:
        print(0)
        continue
    for j in range(i, N-1):
        if time < S[j]:
            time = S[j]
        if ((time-S[j])%F[j]) > 0:
            time += F[j]-(time-S[j])%F[j]
        else:
            time += 0
        time += C[j]
    print(time)