def solve(H, W, A):
    def dfs(row, col, nums):
        if A[row][col] in nums: return 0
        if row == H - 1 and col == W - 1: return 1
        nums.add(A[row][col])
        right = 0 if col == W - 1 else dfs(row, col + 1, nums)
        down =  0 if row == H - 1 else dfs(row + 1, col, nums)
        nums.remove(A[row][col])
        return right + down
    
    return dfs(0, 0, set())

H, W = [int(e) for e in input().split()]
A = [[int(e) for e in input().split()] for _ in range(H)]
print(solve(H, W, A))
