x = [[int(i) for i in input().split()] for i in range(2)]
y = [[int(i) for i in input().split()] for i in range(3)]
p,m,s = [0 for i in range(9)],{},sum(x[0])+sum(x[1])+sum(y[0])+sum(y[1])+sum(y[2])
def ox(t,a):
	if t==9:
		s2 = 0
		for i in range(6):
			if p[i]==p[i+3]: s2+=x[i//3][i%3]
		for i in [0,1,3,4,6,7]:
			if p[i]==p[i+1]: s2+=y[i//3][i%3]
		return s2
	if a and (a in m): return m[a]
	r,n = -10**10,(-1 if t%2 else 1)
	for i in range(9):
		if p[i]==0:
			p[i] = n
			r = max(r,n*ox(t+1,tuple([j for j in p])))
			p[i] = 0
	m[tuple([i for i in p])] = n*r
	return n*r
print(ox(0,None))
print(s-ox(0,None))
