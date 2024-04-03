import sys

def solve(X: int):
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))
    solve(X)
    
    ans = 0
    for i in range(1,1000000):
        ans += i
        if ans >= X:
            print(i)
            exit()
if __name__ == '__main__':
    main()
