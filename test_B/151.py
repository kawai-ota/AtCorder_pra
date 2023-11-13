n,k,m = map(int,input().split())
a = list(map(int,input().split()))
num = sum(a)

#最後のテストの点数を求めている
x = max(0,m * n - num)

if x > k:
  print(-1)
else:
  print(x)