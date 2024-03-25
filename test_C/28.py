import sys
sys.setrecursionlimit = 10**6
from math import inf, factorial
from itertools import accumulate, permutations
from bisect import bisect_left, bisect_right, bisect


def main():
    s = list(map(int, input().split()))
    
    res = set()
    for order in permutations(s):
        res.add(sum(order[:3]))
        
    print(sorted(res, reverse=True)[2])
    
if __name__ == "__main__":
    main()
