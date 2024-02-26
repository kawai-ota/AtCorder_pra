import sys
def gl():
    return list(map(int, sys.stdin.readline().split()))
h, w, n = list(map(int, input().split()))
t = input()
a = [input() for i in range(h)]
cnt = 0
for y in range(h):
    for x in range(w):
        if a[y][x] == '#':
            continue
        ny = y
        nx = x
        ok = True
        for i in range(n):
            if t[i] == 'L': nx -= 1
            elif t[i] == 'R': nx += 1
            elif t[i] == 'U': ny -= 1
            elif t[i] == 'D': ny += 1
            if a[ny][nx] == '#':
                ok = False
                break
        if ok:
            cnt += 1
print(cnt)
