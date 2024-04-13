c_grid = [list(map(int, input().split())) for _ in range(3)]

a_list = [0] * 3
b_list = [0] * 3

for i in range(3):
    b_list[i] = c_grid[0][i] - a_list[0]
    
    
for i in range(1,3):
    a_list[i] = c_grid[i][0] -b_list[0]

is_good = True
for i in range(3):
    for j in range(3):
        if c_grid[i][j] != a_list[i] + b_list[j]:
            is_good = False
            print("No")
            exit()
            
if is_good:
    print("Yes")