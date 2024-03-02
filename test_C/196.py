A = input()
B = len(A)
C = ""
D = ""
if B == 1:
    print(0)
elif B % 2 == 0:
    for i in range(B // 2):
        C += A[i]
    for i in range(B // 2):
        D += A[i + len(A) // 2]
    E = int(C)
    if C > D:
        print(E - 1)
    else:
        print(C)
else:
    A = A[1:]
    E = len(A) // 2
    F = ""
    for i in range(E):
        F += "1"
    print(int(F) * 9)
