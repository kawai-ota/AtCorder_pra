memo={}
memo[1]=0
def f(x):
    if x in memo:
        return memo[x]
    else:
        memo[x]=f(x//2)+f((x+1)//2)+x
        return memo[x]
N=int(input())
print(f(N))