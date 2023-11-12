from itertools import combinations

n = int(input())
d = list(map(int,input().split()))

combinations_result = [x * y for x,y in combinations(d,2)]
ans = 0

for i in combinations_result:
   ans += i

print(ans)