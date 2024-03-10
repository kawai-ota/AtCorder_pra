n, m = map(int, input().split())
s = list(input())
t = [None] * n 
num_col = tuple(map(lambda x: int(x) - 1, input().split()))
col_gr = [[] for _ in range(m)]

for i in range(n):
  col_gr[num_col[i]].append(i)
  
for gr in col_gr:
  l = len(gr)
  
  if l == 1:
    t[gr[0]] = s[gr[0]]
  
  else:
    for i in range(l):
      t[gr[i]] = s[gr[i-1]]
    
print("".join(t))