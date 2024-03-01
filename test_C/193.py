N = int(input())

ans=set()
for i in range(2,int(N**(1/2))+10):
    for j in range(2,int(N**(1/2))+10):
        if i**j<=N:
            ans.add(i**j)
        else:
            break

print(N-len(ans))