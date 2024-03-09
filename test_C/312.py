import bisect

n, m = map(int, input().split())
supply = sorted(list(map(int, input().split())))
demand = sorted(list(map(int, input().split())))

left, right = 0, 10 ** 9 + 1

while right - left > 1:
  mid = (left + right) // 2

  if bisect.bisect(supply, mid) >= m - bisect.bisect_left(demand, mid):
    right = mid
  else:
    left = mid
  
print(right)  