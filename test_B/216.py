n = int(input())
name_list = []

for i in range(n):
  name = tuple(input().split())
  name_list.append(name)

if len(set(name_list)) != n:
   print("Yes")
else:
   print("No")