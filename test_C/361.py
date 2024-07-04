sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

if (sx + sy) % 2 == 1:
    sx -= 1
if (tx + ty) % 2 == 1:
    tx -= 1

x = abs(tx - sx)
y = abs(ty - sy)

# ななめ45度より上の場合
if x < y:
    ans = y
# ななめ45度より下の場合
else:
    ans = (x + y) // 2

print(ans)
