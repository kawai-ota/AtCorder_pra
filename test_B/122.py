S = input()
ans,temp = 0,0
for x in S:
    if x in 'ACGT':
        temp += 1
    else:
        temp = 0
    ans = max(ans,temp)
print(ans)
