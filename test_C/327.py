N, M = 9, 3
A = [list(map(int, input().split())) for _ in range(N)]

row = [set() for _ in range(N)]
col = [set() for _ in range(N)]
blo = [[set() for j in range(M)] for i in range(M)]

for i in range(N):
    for j in range(N):
        row[i].add(A[i][j])
        col[j].add(A[i][j])
        blo[i//M][j//M].add(A[i][j])
if (all(len(r) == 9 for r in row)
    and all(len(c) == 9 for c in col)
    and all(all(len(b) == 9 for b in br) for br in blo)):
    print("Yes")
else:
    print("No")