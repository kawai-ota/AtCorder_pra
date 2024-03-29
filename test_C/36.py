from collections import deque
N = int(input())
A_list = deque()

for i in range(N):
    A_list.append(int(input()))

mes = {d: inx for inx, d in enumerate(sorted(set(A_list)))}

for j in range(N):
    print(mes[A_list.popleft()])
