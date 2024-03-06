N = int(input())
ans = ""
while N>0:
    if N % 2 ==0:
        ans += "B"
        N //= 2
    else:
        ans += "A"
        N -= 1
print(ans[::-1])