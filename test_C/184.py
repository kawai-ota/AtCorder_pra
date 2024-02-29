r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

ans = 3
if r1 == r2 and c1 == c2:
    ans = 0
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
    ans = 1
elif (abs(r1-r2)+abs(c1-c2))<=6 or abs(r1 + c1 - (r2 + c2)) <= 4 or abs((r1 - c1) - (r2 - c2)) <= 4 or ((r1+c1+r2-c2)%2==0 and (r1+c1-r2+c2)%2==0) or ((r1-c1+r2+c2)%2==0 and (r1-c1-r2-c2)%2==0):
    ans = 2
print(ans)
