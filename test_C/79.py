INF = 1 << 60

def calc(data):
    list = [0,0,0]
    for i in range(3):
        if data & (1 << i):
            list[i] = 'A'
        else:
            list[i] = 'B'

    res = int(N[0])
    strin = N[0]
    for i in range(1, 4):
        if list[i-1] == 'A':
            res += int(N[i])
            strin += '+' + N[i]
        else:
            res -= int(N[i])
            strin += '-' + N[i]
    return res, strin


N = input()
data = int(N)

for i in range(8):
    res, strin = calc(i)
    if res == 7:
        print(strin + '=7')
        break
