N, M = map(int, input().split())
A = list(map(int, input().split()))

_lst = result = [0] * N
for a in A:
    _lst[a-1] = 1

_id = "".join(map(str, _lst))

for i in range(N):
    res = _id[i:].find('1')
    print(res)