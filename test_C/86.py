n = int(input())
arr = []

for i in range(n):
    x = list(map(int,input().split()))
    arr.append(x)
prevtime = 0
prevx = 0
prevy = 0


def checker(arr,prevtime,prevx,prevy):
    for i in arr:
        time = i[0]-prevtime
        distx = abs(i[1]-prevx)
        disty = abs(i[2]-prevy)
        mandist = distx +disty
        # print(time)
        # print(distx+disty)
        # print(i[1],i[2])
        
        if time < mandist:
            return -1
        if mandist % 2 != time % 2:
            return -1
        if mandist == 0:
            if (abs(i[1]) + abs(i[2])) % 2 != time % 2:
                return -1

        prevx  = i[1]
        prevy = i[2]
        prevtime = i[0]
    return 1
x = checker(arr, prevtime, prevx, prevy)

if x == 1:
    print('Yes')
else:
    print("No")