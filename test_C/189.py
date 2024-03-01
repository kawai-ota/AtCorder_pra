n = int(input())
a = list(map(int, input().split()))
st = [(0, -1)]
l = [0] * n
for i in range(n):
    while st[-1][0] >= a[i]:
        st.pop()
    l[i] = st[-1][1]
    st.append((a[i], i))

st = [(0, n)]
r = [0] * n
for i in range(n)[::-1]:
    while st[-1][0] >= a[i]:
        st.pop()
    r[i] = st[-1][1]
    st.append((a[i], i))

ans = 0
for i in range(n):
    ans = max(ans, (r[i] - l[i] - 1) * a[i])
print(ans)
