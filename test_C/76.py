S = input()
T = input()
n, m = len(S), len(T)
J = False
for i in reversed(range(n-m+1)):
  J = True
  for j in range(m):
    if S[i+j] != T[j] and S[i+j] != "?":
      J = False
      break
  if J:
    break
if not J:
  print("UNRESTORABLE")
else:
  Ans = ""
  for j in range(n):
    if S[j] == "?":
      Ans += "a"
    else:
      Ans += S[j]
  Ans = Ans[:i] + T + Ans[i+m:]
  print(Ans)