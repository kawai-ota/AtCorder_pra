p,q = map(str,input().split())

distance = {"A":0,"B":3,"C":4,"D":8,"E":9,"F":14,"G":23}

ans = abs(distance[p] - distance[q])
print(ans)