import math
n = int(input().split())
points = [list(map,int(input.split())) for _ in range(n)]

max_distance = 0

for i in range(n):
    for j in range(i,n):
        distance = math.sqrt((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2)
        max_distance = max(distance,max_distance)

print(max_distance)        