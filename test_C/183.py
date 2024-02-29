from itertools import permutations

def count_paths_matching_time(N, K, T):
    cities = list(range(N))
    
    cities.remove(0)
    
    count = 0
    for perm in permutations(cities):
        time = T[0][perm[0]]
        
        for i in range(len(perm) - 1):
            time += T[perm[i]][perm[i + 1]]
        
        time += T[perm[-1]][0]
        
        if time == K:
            count += 1
            
    return count



N, K = map(int, input().split())

T = []
for _ in range(N):
    city = list(map(int, input().split()))
    T.append(city)



print(count_paths_matching_time(N, K, T))