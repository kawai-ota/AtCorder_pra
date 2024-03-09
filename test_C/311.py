N = int(input())
A = list(map(int, ("0 " + input()).split()))
now = 1
for _ in range(N): now = A[now]
B = [now]
while B[0] != A[now]:
	now = A[now]
	B.append(now)
print(len(B))
print(*B)