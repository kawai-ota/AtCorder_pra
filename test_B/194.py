n,x = map(int,input().split())
a = list(map(int,input().split()))

a = [element for element in a if element != a]

for i in a:
  print(i,end = " ")