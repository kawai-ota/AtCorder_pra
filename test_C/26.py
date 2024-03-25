N = int(input())
G = [[] for _ in range(N+1)]
for i in range(2, N+1):
	G[int(input())].append(i)
def rec(v, G):
	if G[v] == []:
		return 1
	S = []
	for v2 in G[v]:
		S.append(rec(v2, G))
	return min(S)+max(S)+1
print(rec(1, G))