n = int(input())
lucas_number = [2,1]

for i in range(2,n + 1):
    lucas_number.append(lucas_number[i - 2] + lucas_number[i - 1])
print(lucas_number[n])    