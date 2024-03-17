deg, dis = map(int, input().split())
deg = (10*deg - 1125) // 2250
ans = ["C", 0]
d = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
if 0<=deg<15 and dis>=15:
    ans[0] = d[deg]
elif dis>= 15:
    ans[0] = "N"
s = 0
l = [3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327]
for i in range(12):
    if 10*dis >= (l[i]*10-5)*6:
        s += 1
ans[1] = s
print(*ans)
