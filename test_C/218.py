def Input():
    L = []
    sx, sy, lx, ly = 10**3, -1, -1, -1
    for i in range(N):
        s = input()
        if '#' in s:
            if sy == -1:
                sy = i
            sx = min(sx, s.index('#'))
            lx = max(lx, s.rfind('#'))
            ly = i
        L.append(s)
    L2 = []
    for y in range(sy, ly + 1):
        L2.append(tuple(L[y][sx:lx + 1]))
    return L2


def rot90(S):
    return [i for i in zip(*S[::-1])]


def check(S, T):
    if len(S) != len(T):
        return False
    for s, t in zip(S, T):
        if s != t:
            return False
    return True


N = int(input())
S, T = Input(), Input()

for _ in range(4):
    if check(S, T):
        print("Yes")
        exit()
    S = rot90(S)
print("No")
