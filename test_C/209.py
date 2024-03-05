N = int(input())
C = list(map(int, input().split()))
C.sort()

mod = 10 ** 9 + 7

answer = C[0]
for i in range(1,N):
    if C[i] < i:
        answer = 0
        break

    answer = (answer * (C[i] - i)) % mod

print(answer)