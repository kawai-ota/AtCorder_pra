x,y,z = map(int,input().split())
count = 0

while (y + 2 * z) <= x:
    x = x - (y + z)
    count += 1

print(count)    