def slopes_calc(points):
    ans = "No"
    for i in range(M-1):
        slopes_list = []
        for j in range(i+1,M):
            x1, y1 = points[i]
            x2, y2 = points[j]
        
            if x2 == x1:
                slope_p1_p2 = "infinite"
            else:
                slope_p1_p2 = (y2-y1)/(x2-x1)
            
            if slope_p1_p2 in slopes_list:
                ans = 'Yes'
                break
            slopes_list.append(slope_p1_p2)
            
    return ans

M = int(input())
points = [tuple(map(int,input().split())) for k in range(M)]
ans = slopes_calc(points)
print(ans)