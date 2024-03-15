N, M = map(int, input().split())
S = input()
ans = 0
T, L = 0, 0

for i in range(N):
    if S[i] == '0':
        ans = max(ans, (T + L) - min(M, T))
        T = 0
        L = 0
    if S[i] == '1':
        T += 1
    if S[i] == '2':
        L += 1
else:
    ans = max(ans, (T + L) - min(M, T))

print(ans)
