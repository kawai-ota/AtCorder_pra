n = int(input())
s = input()

if len(s) == 1:
    print(1)

else:
    c = s[0]
    ans = [0] * 26
    r = 1
    for i in range(1, n+1):
        if i == n:
            ans[ord(s[i-1])-97] = max(r, ans[ord(s[i-1])-97])
            r = 1
            break
                       
        elif s[i] == c:
            r += 1
            
        else:
            ans[ord(s[i-1])-97] = max(r, ans[ord(s[i-1])-97])
            r = 1
            c = s[i]
            
    print(sum(ans))
