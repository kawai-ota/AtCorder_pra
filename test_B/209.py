n,x = map(int,input().split())
a = list(map(int,input().split()))
count = 0

for i in range(1,len(a),2):
    a[i] -= 1

for j in a:
    count += j

if count <= x:
    print("Yes")
else:
    print("No")            