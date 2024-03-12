import itertools

belong_line = [
    [0, 3, 6],
    [0, 4],
    [0, 5, 7],
    [1, 3],
    [1, 4, 6, 7],
    [1, 5],
    [2, 3, 7],
    [2, 4],
    [2, 5, 6]
]

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

c = r1 + r2 + r3

p = list(range(9))

disappointed_cnt = 0
total_cnt = 0 

for perm in itertools.permutations(p):
    disappointed = False
    total_cnt += 1
    route = [[] for _ in range(8)]
    for x in perm:
        for line_id in belong_line[x]:
            route[line_id].append(c[x])
            if (len(route[line_id]) == 2) and (route[line_id][0] == route[line_id][1]):
                disappointed = True
    
    if disappointed is True:
        disappointed_cnt += 1
        
p = (total_cnt - disappointed_cnt) / total_cnt
print(f"{p:.12f}")