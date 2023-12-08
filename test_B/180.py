import math
n = int(input())
x = list(map(int,input().split()))

ans_1 = 0
ans_2 = 0
ans_3 = []

for i in range (n):
  ans_1 += abs(i)
  ans_2 += abs(i) ** 2
  ans_3.append(abs(i))

ans_2 = math.sqrt(ans_2)

print(ans_1)
print(ans_2)
print(max(ans_3))