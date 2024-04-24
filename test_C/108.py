def solve(N, K):
    if K % 2 == 0:
        x = N // K
        y = (N + K // 2) // K
        return x * x * x + y * y * y
    else:
        x = N // K
        return x * x * x

N, K = map(int, input().split())
print(solve(N, K))
