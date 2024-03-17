xa, ya, xb, yb, xc, yc = map(int, input().split())
S = abs((xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)) / 2
print(S)