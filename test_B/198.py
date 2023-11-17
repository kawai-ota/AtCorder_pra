n = list(input())
while n and n[-1] == '0':
    n.pop()

l = 0
r = len(n) - 1
while r - l > 0:
    if n[r] == n[l]:
        l += 1
        r -= 1
    else:
        print("No")
        break

else:
    print("Yes")        
