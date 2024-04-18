s = input()
K = int(input())
N = len(s)
st = set()
cmin = "zz"
for i in range(N):
    for j in range(i+1, N+1):
        if j - i > 10:
            break
        ss = s[i:j]
        st.add(ss)
L = list(st)
L.sort()
print(L[K-1])
