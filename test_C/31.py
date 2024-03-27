N = int(input())
a = list(map(int, input().split()))

odd = [0]
even = [0]
for i in range(N):
    if i % 2 == 0:
        odd.append(odd[-1] + a[i])
        even.append(even[-1])
    else:
        odd.append(odd[-1])
        even.append(even[-1] + a[i])

answer = -float("inf")
for i in range(N):
    candidate_aoki = float("inf")
    candidate_j = -1
    candidate_takahashi = -float("inf")

    for j in range(i):
        if j % 2 == 0:
            if candidate_j == -1 or even[i + 1] - even[j] > candidate_aoki:
                candidate_j = j
                candidate_aoki = even[i + 1] - even[candidate_j]
                candidate_takahashi = odd[i + 1] - odd[candidate_j]
        else:
            if candidate_j == -1 or odd[i + 1] - odd[j] > candidate_aoki:
                candidate_j = j
                candidate_aoki = odd[i + 1] - odd[candidate_j]
                candidate_takahashi = even[i + 1] - even[candidate_j]

    for j in range(i + 1, N):
        if i % 2 == 0:
            if candidate_j == -1 or even[j + 1] - even[i] > candidate_aoki:
                candidate_j = j
                candidate_takahashi = odd[candidate_j + 1] - odd[i]
                candidate_aoki = even[candidate_j + 1] - even[i]
        else:
            if candidate_j == -1 or odd[j + 1] - odd[i] > candidate_aoki:
                candidate_j = j
                candidate_takahashi = even[candidate_j + 1] - even[i]
                candidate_aoki = odd[candidate_j + 1] - odd[i]

    answer = max(answer, candidate_takahashi)

print(answer)
