T = int(input())
N = int(input())
TAKOYAKI = list(map(int,input().split()))+[0]
M = int(input())
CUSTOMER = list(map(int,input().split()))+[0]
takoyaki = []
customer = []

for i in range(1,101):
    if len(customer) != 0:
        print("no")
        break
    gomi = 0
    for j in range(len(takoyaki)):
        takoyaki[j] += 1
        if takoyaki[j] > T:
            gomi += 1
    for j in range(gomi):
        takoyaki.pop(0)

    while TAKOYAKI[0] == i:
        takoyaki.append(0)
        TAKOYAKI.pop(0)
    while CUSTOMER[0] == i:
        customer.append(0)
        CUSTOMER.pop(0)
    a = min([len(customer),len(takoyaki)])
    for j in range(a):
        takoyaki.pop(0)
        customer.pop(0)

if len(customer) == 0 and len(CUSTOMER) == 1:
    print("yes")

