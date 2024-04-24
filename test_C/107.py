def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    pos = [x for x in arr if x >= 0]
    neg = [-x for x in arr if x < 0]

    neg.reverse()
    mini = 10**18
    if len(pos) >= k:
        mini = min(mini, pos[k-1])
    if len(neg) >= k:
        mini = min(mini, neg[k-1])
    for i in range(len(pos)):
        if i < k:
            on_left = k - i - 1
            if len(neg) >= on_left and on_left > 0:
                a = pos[i]
                b = neg[on_left-1]
                mini = min(mini, 2 * a + b, 2 * b + a)
    print(mini)

if __name__ == "__main__": 
    t = 1
    for i in range(1, t + 1):
        solve()
