A, B, C = map(int, input().split())
abc = list([A, B, C])
abc.sort()
cnt = 0
cnt += abc[2] - abc[1]
abc[2] -= cnt
p = (abc[1] - abc[0]) // 2
if (abc[1] - abc[0]) % 2 == 0:
    print(cnt + p)
else:
    print(cnt + p + 2)
