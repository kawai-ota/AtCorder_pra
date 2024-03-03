n, k = map(int, input().split())
friends = []
for i in range(n):
    a, b = map(int, input().split())
    friends.append((a, b))

friends.sort(key=lambda x: x[0])

now_money, now_position = k, 0
for i in range(n):
    dist = friends[i][0] - now_position
    if dist <= now_money:
        now_position = friends[i][0]
        now_money = now_money - dist + friends[i][1]
    else:
        now_position += now_money
        print(now_position)
        exit(0)

print(now_position + now_money)