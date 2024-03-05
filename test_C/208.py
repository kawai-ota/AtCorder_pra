N,K=map(int,input().split())
a=(list(map(int,input().split())))
jun=[]
kihon=K//N
for i,v in enumerate(a):
    jun.append([i,v,kihon])
        
kihon=K//N
amri=K%N
jun.sort(key=lambda x:x[1])
for i in range(amri):
    jun[i][2]+=1
            
jun.sort()
for i in range(N):
    print(jun[i][2]) 