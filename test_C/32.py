from heapq import heappush, heappop, heapify
import sys
import copy
from collections import defaultdict, deque
from math import ceil, floor, sqrt, factorial, gcd
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10**7)
# input = sys.stdin.readline
vector1 = [[0, -1], [1, 0], [0, 1], [-1, 0]]
vector2 = [[0, 1], [1, 0], [-1, 0], [0, -1],
           [1, -1], [-1, 1], [1, 1], [-1, -1]]


def main():
    N, K = map(int, input().split())
    s = [int(input()) for i in range(N)]
    seki = 1
    ans = 0
    right = 0
    
    if 0 in s:
        print(N)
        exit()
    
    for left in range(N):
        while (right < N and seki * s[right] <= K):
            seki *= s[right]
            right += 1

        ans = max(ans, right-left)
        if right == left:
            right += 1
        else:
            seki = seki // s[left]
    print(ans)


if __name__ == '__main__':
    main()
