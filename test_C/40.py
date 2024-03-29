def main() -> None:
    import sys

    input = sys.stdin.readline

    n = int(input())
    A = list(map(int, input().split()))

    dp = [1 << 60] * n
    dp[0] = 0
    for i in range(n):
        if i + 1 < n:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(A[i] - A[i + 1]))
        if i + 2 < n:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(A[i] - A[i + 2]))

    print(dp[n - 1])


if __name__ == "__main__":
    main()
