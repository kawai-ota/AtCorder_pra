def main():
    R, C = map(int, input().split())
    S = tuple(map(int, input().split()))
    G = tuple(map(int, input().split()))
    M = []
    for _ in range(R):
        M.append(list(input())) 
    now = [S[0]-1, S[1]-1]
    queue = []
    kyori = [[-1] * C for _ in range(R)]
    kyori[now[0]][now[1]] = 0
    while 1:
        if now[0] == G[0]-1 and now[1] ==  G[1]-1:
            print(kyori[now[0]][now[1]])
            return
        for i, j in [(-1,0),(0,-1),(0,1),(1,0)]:
            next = [now[0] + i, now[1] + j]
            if M[next[0]][next[1]] == '.' and kyori[next[0]][next[1]] == -1:
                queue.append(next)
                kyori[next[0]][next[1]] = kyori[now[0]][now[1]] + 1
        now = queue.pop(0)

if __name__ == "__main__":
    main()
