H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
f = False
coords = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            coords.add((h, w))


for coord in coords:
    if (
        (coord[0] - 1, coord[1]) not in coords
        and
        (coord[0] + 1, coord[1]) not in coords
        and
        (coord[0], coord[1] - 1) not in coords
        and
        (coord[0], coord[1] + 1) not in coords
    ):
        print("No")
        break
else:
    print("Yes")


