N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

S1 = [0] * (N+1)
S2 = [0] * (N+1)

for i in range(N):
  S1[i+1] = S1[i] + A1[i]
  S2[i+1] = S2[i] + A2[i]
  
max_candy_num = 0
for i in range(N):
  candy_num = (S1[i+1]) + (S2[N] - S2[i])
  if max_candy_num < candy_num:
    max_candy_num = candy_num
    
print(max_candy_num)