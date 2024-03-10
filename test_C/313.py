N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

b = 0
L = []
for i in range(N):
  for j in range(b, M):
    if A[i] <= B[j]:
      if M-j <= i+1:
        print(min(A[i], B[-(i+1)]+1))
        exit()
      else:
        b = j
        break
  else:
    print(B[-(i+1)]+1)
    exit()
else:
  print(B[-(N+1)]+1)