n,m = map(int,input().split())
x = [*map(int,input().split())]
x.sort()
intervals = []
for i in range(len(x)-1):
    intervals.append(x[i+1]-x[i])
intervals.sort(reverse=True)
print(sum(intervals[n-1:]))