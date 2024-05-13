import sys
sys.setrecursionlimit(5*10**7)
def Lis():
    return list(input()) #ひとつひとつの「文字」をリストにしてインプット
def IR(N): #N行整数をリスト化
    x = []
    for _ in range(N):
        x.append(int(input())) 
    return x
def SR(N): #N行文字列をリスト化
    x = []
    for _ in range(N):
        x.append(input())
    return x
def IRM(N): #列に変数が並ぶN行データ
    z = [map(int, input().split()) for _ in range(N)]
    return [list(i) for i in zip(*z)]
def SGrid(N): #N行文字列二次元グリッドをリスト化
    x = []
    for i in range(N):
        x.append(list(input()))
    return x
def IMatrix(N): #一般のN行行列
    return [list(map(int, input().split())) for l in range(N)]
def igraph(N, M, directed = True): #N, Mと枝指定のグラフ入力: N => node, M => edge, directed = True(有向) False(無向)
    G = [set() for i in range(N)]
    into_num = [0 for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        # node A to B
        G[a-1].add(b-1)
        into_num[b-1] += 1
        if not directed:
            # node B to A
            G[b-1].add(a-1)
    return G, into_num
def yesno(judge: bool, t="Yes", f='No'):
    if judge:
        print(t)
    else:
        print(f)

def bi(i:int, n: int): #iをn桁の2進数に変換
    return format(i, '0' + str(n) + 'b')
    
def mod(bunbo, bunsi, mod = 998244353):
    denominator = pow(bunbo, -1, mod)
    return bunsi * denominator % mod
def ST():
    return input() #str型
def IN():
    return int(input()) #int型
def FL():
    return float(input()) #float型
def SL():
    return input().split() #strリスト・複数列併用
def IM():
    return map(int, input().split()) #int複数列
def IL():
    return list(map(int, input().split())) #intリスト
def IS():
    return set(map(int, input().split())) #intリスト
import math
import bisect  #二分探索 
import heapq
from collections import deque, defaultdict 
import random

N = IN()

ans = 0

for i in range(1, 5000):
    for j in range(i, int(math.sqrt(N//i))+2):
        k = N//(i*j)
        if k >= j:
            ans += k-j+1

print(ans)
