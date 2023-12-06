N = int(input())
X = []
Y = []

for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)
res = 0
for i in range(N):
    for j in range(i+1, N):
        if -1 <= (Y[i] - Y[j]) / (X[i] - X[j]) <= 1:
            res += 1
print(res)