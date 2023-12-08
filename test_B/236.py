n = int(input())
a = list(map(int ,input().split()))
cnt = [0] * (n + 1)
for i in a:cnt[i] += 1
for i in set(a):
    if cnt[i] != 4:
        print(i)
        break