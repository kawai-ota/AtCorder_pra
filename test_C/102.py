import bisect
n = int(input())
a = list(map(int, input().split()))
bs = sorted([e-i for i, e in enumerate(a, 1)])
ps = [0]
for i in range(n):
	ps.append(ps[-1]+abs(bs[i]))


def f(x):
	i = bisect.bisect_right(bs, x)
	j = bisect.bisect_left(bs, 0)
	fa = -(j-i)*x
	if i>j: i, j = j, i
	l = ps[i]+x*i
	f = ps[i]-ps[j]+fa
	u = ps[-1]-ps[j]-(n-j)*x
	return l+f+u


l, r = bs[0], bs[-1]+1
while l<r:
	m = (l+r)//2
	if f(m)<f(m+1):
		r = m
	else:
		l = m+1
print(f(l))