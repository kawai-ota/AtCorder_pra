N = int(input())
A = list(map(int, input().split()))
m = {A[x]: x+1 for x in range(N)}
ans = []
ans.append(m[-1])
for _ in range(N-1):
  ans.append(m[ans[-1]])

ans_str = " ".join(map(str, ans))

print(ans_str)