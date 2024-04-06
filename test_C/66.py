N = int(input())
A = list(map(int,input().split()))
odd = []
even = []

for i in range(N):
  if i % 2 == 0:
      odd.append(A[i])  
  else:
      even.append(A[i])


if N % 2 == 0:
    even.reverse()
    print(*even, *odd)
else:
    odd.reverse()
    print(*odd, *even)