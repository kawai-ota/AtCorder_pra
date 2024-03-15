digits = []
N = int(input())
#N=1
N -= 1
divisor = 5
while divisor < N:
  divisor *= 5

while divisor >= 5:
  if divisor <= N:
    digits.append(N//divisor)
    N%=divisor
  else:
    digits.append(0)
  divisor //= 5
digits.append(N)

leading_zero = True
for d in digits:
  if leading_zero and d == 0:
    continue
  if d: leading_zero = False
  print(2*d, end="")
if leading_zero: print(0)
else: print("")
