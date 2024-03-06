from itertools import permutations

S, N = input().split()
S = list(S)
N = int(N)

L = list(permutations(S))
T1 = ["".join(l) for l in L]
T2 = set(T1)
T3 = list(T2)
T3.sort()

    
print(T3[N-1])