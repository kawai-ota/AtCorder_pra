from itertools import permutations

N, M = map(int, input().split())
edges = {i: set() for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

def count_paths():
    count = 0
    for perm in permutations(range(2, N+1)):
        valid = True
        current = 1
        for next_vertex in perm:
            if next_vertex not in edges[current]:
                valid = False
                break
            current = next_vertex
        if valid:
            count += 1
    return count

print(count_paths())
