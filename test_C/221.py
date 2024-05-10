S = input()
N = len(S)
ans = []
def chenge(N):
    R = ''
    while N >= 1:
        if N % 2 == 1:
            R = '1'+R
        else:
            R = '0'+R
        N //= 2
    return R
for i in range(2**N):
    s = chenge(i)
    a = ''
    b = ''
    s = '0'*(N-len(s))+s
    for j in range(len(s)):
        if s[j] == '0':
            a += S[j]
        else:
            b += S[j]
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    aa = 0
    bb = 0
    for j in range(len(a)):
        aa += int(a[j])*10**(len(a)-j-1)
    for j in range(len(b)):
        bb += int(b[j])*10**(len(b)-j-1)
    ans.append(aa*bb)

print(max(ans)
      )
