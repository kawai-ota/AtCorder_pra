n,m = map(int,input().split())
a = list(map(int,input().split()))
arr_num = sum(a)
num = arr_num // 4 * m

count = 0

for i in a:
  if i >= num:
    count += 1

if count >= m:
   print("Yes")
else:
   print("No")