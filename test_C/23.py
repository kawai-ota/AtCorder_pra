from sys import stdin; input = stdin.readline
from heapq import heappush, heappop

def solv(N, G, tgt, l):
	dist = [1<<60]*N
	dist[0] = l
	Q = [(l, 0)]
	while Q:
		d, v = heappop(Q)
		if dist[v] < d: continue
		if v == tgt: return d
		for v_nxt, d_nxt in G[v]:
			if v==0 and v_nxt==tgt: continue
			if d+d_nxt < dist[v_nxt]:
				dist[v_nxt] = d+d_nxt
				heappush(Q, (d+d_nxt, v_nxt))
	return dist[tgt]

def main():
	N, M = map(int, input().split())
	UVL = [list(map(int, input().split())) for _ in range(M)]
	G = [[] for _ in range(N)]
	for u, v, l in UVL:
		u-=1; v-=1
		G[u].append((v, l))
		G[v].append((u, l))
	ans = 1<<60
	for x, l in G[0]:
		ans = min(ans, solv(N, G, x, l))
	print([ans, -1][ans==1<<60])

if __name__ == '__main__': main()
