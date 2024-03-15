from collections import deque

n , k = map(int,input().split())
A = list(map(int,input().split()))

if k % 2 == 0 :
  ans = 0
  for i in range(0 , k - 1 , 2) :
    ans += A[i + 1] - A[i]
  print(ans)
  exit()
  
left = deque()

for i in range(0 , k - 1 , 2) :
  left.append(A[i + 1] - A[i])
  
right = deque()  
  
for i in range(1 , k - 1 , 2) :
  right.append(A[i + 1] - A[i])
  
total = sum(left)
ans = total

while left and right :
  x = left.pop()
  y = right.pop()
  total = total - x + y
  ans = min(ans , total)
  
print(ans)

