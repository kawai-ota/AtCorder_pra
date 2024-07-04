n = int(input())

l = [['#'],
     ['###',
      '#.#',
      '###'],
     ['#########',
      '#.##.##.#',
      '#########',
      '###...###',
      '#.#...#.#',
      '###...###',
      '#########',
      '#.##.##.#',
      '#########']]

c = len(l) - 1
if n <= c:
    for i in range(len(l[n])):
        print(l[n][i])
    exit()

while c != n:
    g = []
    for i in range(len(l[c])):
        row = l[c][i] * 3
        g.append(row)
    g2 = []
    for i in range(len(l[c])):
        row2 = l[c][i] + '.'*len(l[c][i]) + l[c][i]
        g2.append(row2)
    grid = g + g2 + g
    l.append(grid)
    c += 1

for i in range(len(l[n])):
    print(l[n][i])
