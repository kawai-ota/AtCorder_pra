N = int(input())
count = 0

def ten(x):
    x = str(x)
    if '7' in x:
        return True
    else:
        return False

def eight(x):
    s = ""
    while x>0:
        s = str(x % 8)+s
        x //= 8
    if '7' in s:
        return True
    else:
        return False

for i in range(1,N+1):
    if ten(i) == False and eight(i) == False:
        count += 1
print(count)