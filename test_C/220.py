n=int(input())
A=list(map(int,input().split()))
sm=sum(A)
z=int(input())
ans = z//sm * n
cur=sm* (z//sm)

for i in range(n):
  cur+=A[i]
  ans+=1
  if cur>z:  break
  
print(ans)