n=int(input())
a=list(map(int,input().split()))

def judge(p):
  cum=0
  cnt=0
  for i in range(n):
    cum+=a[i]
    if i%2==p and cum<=0:
      cnt+=abs(cum)+1
      cum=1
    elif i%2!=p and cum>=0:
      cnt+=abs(cum)+1
      cum=-1
  return cnt
print(min(judge(0),judge(1)))