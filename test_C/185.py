L = int(input())

fact = [1]*L
for i in range(1,L):
  fact[i] = i*fact[i-1]

def nCr(n,r):
  return fact[n]//(fact[n-r]*fact[r])
  
print(nCr(L-1,11))