from sys import stdin


readline = stdin.readline
a, b, c, d, e, f = map(int, readline().split())
ff = (f + 100) // 100 + 1
dp = [[False] * ff * e for _ in [0] * ff]
dp[0][0] = True


def check(w, s):
    return w * e - 100 * s >= 0


for w in range(ff):
    for s in range(ff * e):
        if not dp[w][s]:
            continue
        if check(100 * w, s + c):
            dp[w][s + c] = True
        if check(100 * w, s + d):
            dp[w][s + d] = True

        if w + a < ff:
            dp[w + a][s] = True
        if w + b < ff:
            dp[w + b][s] = True


def compare(w1, s1, w2, s2):
    return s1 * (w2 + s2) - s2 * (w1 + s1) >= 0


ans_w, ans_s = 0, 0
for w in range(ff):
    for s in range(ff * e):
        if not dp[w][s]:
            continue
        if 100 * w + s > f:
            continue
        if compare(100 * w, s, ans_w, ans_s):
            ans_w = 100 * w
            ans_s = s

print(ans_w + ans_s, ans_s)
