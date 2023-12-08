k = int(input())
a,b = map(str,input().split())
ans_1 = 0
ans_2 = 0

for i in range(len(a)):
  ans_1 += int(a[i]) * (k ** (len(a) - (i + 1)))
  
for j in range(len(b)):
  ans_2 += int(b[j]) * (k ** (len(b) - (j + 1)))
  
sum = ans_1 * ans_2

print(sum)