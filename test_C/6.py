N,M=map(int,input().split())
if M>4*N:
    a=b=c=-1
elif M>3*N:
    c=M-3*N
    b=N-c
    a=0
elif M>=2*N:
    c=0
    b=M-2*N
    a=N-b
else:
    a=b=c=-1
print(a,b,c)
