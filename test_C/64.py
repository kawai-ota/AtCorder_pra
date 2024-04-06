N = int(input())
A = list(map(int, input().split()))

types = 0
free = 0
player = [0 for num in range(8)]

for item in A:
    pos = int(item//400)
    if(pos < 8):
        if(player[pos] == 0):
            player[pos] += 1
            types += 1
    else:
        free += 1

print(f'{max(1, types)} {types + free}')
    