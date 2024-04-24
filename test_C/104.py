D, G = map(int, input().split())
P = []
C = []
for i in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

ans = float('inf')
for bit in range(1<<D):
    score = 0
    problems_solved = 0
    for i in range(D):
        if bit & (1<<i):
            score += 100 * (i+1) * P[i] + C[i]
            problems_solved += P[i]
    for i in range(D-1, -1, -1):
        if bit & (1<<i):
            continue
        for _ in range(P[i]):
            if score >= G:
                ans = min(ans, problems_solved)
                break
            score += 100 * (i+1)
            problems_solved += 1
    if score >= G:  # If the score is at least G, update the minimum number of problems solved
        ans = min(ans, problems_solved)

print(ans)