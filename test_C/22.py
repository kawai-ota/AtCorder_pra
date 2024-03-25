import heapq

def dijkstra(next_nodes, s, t):
    fix = {}
    seen = {s:0}
    queue = []
    heapq.heappush(queue, (0, s))
    while len(queue) > 0:
        cost, v = heapq.heappop(queue)
        if v in fix:
            continue

        fix[v] = cost
        if v == t:
            break

        for w, l in next_nodes[v].items():
            if w in fix:
                continue

            if (s, t) in ((v, w), (w, v)):
                continue

            new_cost = cost + l
            if w not in seen or seen[w] > new_cost:
                seen[w] = new_cost
                heapq.heappush(queue, (new_cost, w))

    if t in fix:
        return fix[t]
    else:
        return float("inf")


def main():
    N, M = map(int, input().split())
    next_nodes = [{} for _ in range(N)]
    for _ in range(M):
        u, v, l = map(int, input().split())
        next_nodes[u - 1][v - 1] = l
        next_nodes[v - 1][u - 1] = l


    answer = float("inf")
    for s, l in next_nodes[0].items():
        cost = dijkstra(next_nodes, s, 0)
        cost += l
        answer = min(answer, cost)
    
    if answer == float("inf"):
        print(-1)
    else:
        print(answer)




if __name__ == "__main__":
    main()