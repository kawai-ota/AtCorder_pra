N, M = map(int, input().split())
A = list(map(int, input().split()))
result = []

for i in range(N):
    S = input()
    score = i+1
    not_solved = []
    for j in range(len(S)):
        if S[j] == "o":
            score += A[j]
        else:
            not_solved.append(A[j])
    not_solved.sort()
    result.append((score, not_solved))

max_socre = max([result[i][0] for i in range(N)])

for i in range(N):
    score, not_solved = result[i]
    cnt= 0
    while True:
        if score >= max_socre:
            print(cnt)
            break

        score += not_solved.pop()
        cnt += 1
