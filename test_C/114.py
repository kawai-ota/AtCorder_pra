N = int(input())

def solve(s):
  if int(s) > N:
    return 0
  res = solve(s + "3") + solve(s + "5") + solve(s + "7")
  if "3" in s and "5" in s and "7" in s:
    res += 1
  return res

print(solve("3") + solve("5") + solve("7"))