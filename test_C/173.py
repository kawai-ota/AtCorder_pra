import copy

def paint_red_row(g: list, row: int):
    for i in range(len(g[0])):
        g[row][i] = 'R'

def paint_red_col(g: list, col: int):
    for i in range(len(g)):
        g[i][col] = 'R'

def count_black(g: list):
    count = 0
    for row in g:
        for cell in row:
            if cell == '#':
                count += 1
    return count

h, w, k = map(int, input().split())
g = []
for _ in range(h):
    g.append(list(input()))

ans = 0
for bit1 in range(2 ** h):
    for bit2 in range(2 ** w):
        g_copy = copy.deepcopy(g)
        for i in range(h):
            if (bit1 >> i) & 1:
                paint_red_row(g_copy, i)
        for i in range(w):
            if (bit2 >> i) & 1:
                paint_red_col(g_copy, i)
        black_count = count_black(g_copy)
        if black_count == k:
            ans += 1
print(ans)
