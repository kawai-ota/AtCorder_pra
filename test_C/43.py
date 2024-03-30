import math

n = int(input())
arr = list(map(int, input().split()))  

sums = sum(arr)
if sums % len(arr) == 0:
    avg_1 = int(sums / len(arr))
    avg_2 = avg_1
else:
    avg_1 = math.ceil(sums / len(arr))
    avg_2 = math.floor(sums / len(arr))
ans_1 = 0
ans_2 = 0
for i in arr:
    ans_1 = ans_1 + (avg_1 - i) * (avg_1 - i)
    ans_2 = ans_2 + (avg_2 - i) * (avg_2 - i)

    
print(min(ans_1,ans_2))
