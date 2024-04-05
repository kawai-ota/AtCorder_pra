n=int(input())
box=[]
count=0
for i in range(n):
    box.append(int(input()))
    count+=box[i]

if count%10!=0:
    print(count)
else:
    ans=0
    for i in range(n):
        if (count-box[i])%10!=0:
            ans=max(ans,count-box[i])
    print(ans)