H, W = map(int, input().split())
S = [input() for _ in range(H)]


def is_vert(y, x):
    if not (0 <= y+1 < H and 0 <= x+1 < W):
        return False
    cnt = 0
    if S[y][x] == '#':
        cnt += 1
    if S[y+1][x] == '#':
        cnt += 1
    if S[y][x+1] == '#':
        cnt += 1
    if S[y+1][x+1] == '#':
        cnt += 1

    if cnt == 1 or cnt == 3:
        return True
    return False


ans = 0
for i in range(H):
    for j in range(W):
        if is_vert(i, j):
            ans += 1
print(ans)
