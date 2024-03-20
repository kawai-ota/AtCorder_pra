from collections import deque

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
dh = (-1, 0, 1, 0)
dw = (0, -1, 0, 1)

Q = deque()
for h, s in enumerate(S):
    for w, c in enumerate(s):
        if c == 'x':
            dist[h][w] = 0
            Q.append((h, w))

while Q:
    h, w = Q.popleft()
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0 <= nh < H and 0 <= nw < W and dist[nh][nw] == -1:
            if dist[h][w] + 1 >= K:
                continue
            dist[nh][nw] = dist[h][w] + 1
            Q.append((nh, nw))

ans = 0
for h in range(K - 1, H - (K - 1)):
    ans += dist[h][K - 1:W - (K - 1)].count(-1)
print(ans)
