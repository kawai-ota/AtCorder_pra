import sys
input = sys.stdin.readline
mod = 10**9 + 7
inf = float('inf')


def main():
    n, h = map(int, input().split())
    a, b, c, d, e = map(int, input().split())

    def f(x, y):
        return x * a + y * c
    ans = inf
    for x in range(n+1):
        y = min(max(((-1*x*(b+e) - h + n*e)//(d+e))+1, 0), n-x)
        ans = min(ans, f(x, y))
    print(ans)
    
if __name__ == '__main__':
    main()