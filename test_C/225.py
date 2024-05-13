N, M = map(int, input().split())
Bnm = [list(map(int, input().split())) for _ in range(N)]

def ischeck(nums, n):
    for i in range(len(nums)-1):
        if nums[i] + n != nums[i+1]:
            return False
    return True

def solve():
    for i in range(N):
        if not ischeck(Bnm[i], 1):
            return False
        if (Bnm[i][0] + 6) // 7 != (Bnm[i][-1] + 6) // 7:
            return False
    
    Bnm_t = [list(x) for x in zip(*Bnm)]
    for i in range(M):
        if not ischeck(Bnm_t[i], 7):
            return False
    
    return True

print('Yes' if solve() else 'No')
