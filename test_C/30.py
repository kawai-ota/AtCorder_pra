N,M = map(int, input().split())
X,Y = map(int, input().split())
a = list(map(int, input().split()))+[10**18]
b = list(map(int, input().split()))+[10**18]

now = 0

now_a = 0
now_b = 0
cnt = 0
for i in range(N+M):
    a_ok = 0
    b_ok = 0

    for j in range(now_a,N):

        if now <= a[j]:
            now = a[j]+X
            now_a += 1
            a_ok = 1
            break

        now_a += 1


    for j in range(now_b,M):

        if now <= b[j]:
            now = b[j]+Y
            now_b += 1
            b_ok = 1
            break

        now_b += 1

    if a_ok == 1 and b_ok == 1:
        cnt += 1
print(cnt)