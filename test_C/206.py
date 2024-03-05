n = int(input())
c = n*(n-1)//2
nums = list(map(int,input().split()))
mapNums = {}
ans = 0

for i in range(n):
    if nums[i] in mapNums:
        mapNums[nums[i]] += 1
    else:
        mapNums[nums[i]] = 1



for num in mapNums.values():
    ans += (n - num) * num
    n -= num

print(ans)
