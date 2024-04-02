N,K=map(int,input().split())
A=set(map(int,input().split()))

print(K*(K+1)//2-sum(x for x in A if x<=K))
