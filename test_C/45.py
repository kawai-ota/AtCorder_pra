S = input()
ans = 0


def solve(i, s, c):
    global ans
    if i == len(S):
        ans += s
        return
    if i != len(S) - 1:
        solve(i + 1, s, c + S[i])
    solve(i + 1, s + int(c + S[i]), "")


solve(0, 0, "")
print(ans)
