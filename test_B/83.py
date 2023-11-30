n,a,b = map(int,input().split())
ans = 0

for i in range(1,n + 1):
    key = str(i)
    digit_sum = sum(int(digit) for digit in key)

    if a <= digit_sum <= b:
        ans += digit_sum

print(ans)