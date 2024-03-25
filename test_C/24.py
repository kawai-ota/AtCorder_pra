import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, D, K = map(int, readline().decode("utf-8").rsplit(" "))

LR = [list(map(int, readline().decode("utf-8").rsplit(" "))) for _ in range(D)]

for _ in range(K):
    s, t = map(int, readline().decode("utf-8").rsplit(" "))
    if t > s:
        for i, (li, ri) in enumerate(LR):
            if li <= s <= ri:
                if t <= ri:
                    print(i + 1)
                    break
                else:
                    s = ri
    else:
        for i, (li, ri) in enumerate(LR):
            if li <= s <= ri:
                if t >= li:
                    print(i + 1)
                    break
                else:
                    s = li
