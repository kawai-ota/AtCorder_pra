a, b = map(int, input().split())

key = str(a) + str(b)
num = int(key)

i = 1

while i * i <= num:
    if i * i == num:
        print("Yes")
        exit()
    i += 1    

print("No")        