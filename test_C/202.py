from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))

ca = Counter(A)
ans = 0
for c in C:
    ans += ca[B[c]]
print(ans)
