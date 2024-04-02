x=int(input())
a=x//11
b=x%11
if b==0:
    print(2*a)
elif b<=6:
    print(2*a+1)
else:
    print(2*a+2)