n, k = map(int, input().split())
a = list(map(int, input().split()))

can_use = [i for i in range(0, 10) if i not in a]
digits = str(n)

ans = ""
changes = False

if int(digits[0]) not in can_use:
    flag = False
    for num in can_use:
        if int(digits[0]) < num:
            ans += str(num)
            flag = True
            break

    if flag:
        for i in range(1, len(digits)):
            ans += str(can_use[0])
        print(ans)
    else:
        if can_use[0] == 0:
            ans += str(can_use[1])
        else:
            ans += str(can_use[0])

        for i in range(1, len(digits)):
            ans += str(can_use[0])

        ans += str(can_use[0])
        print(ans)

else:
    flag = False
    ok = False
    for i, char in enumerate(digits):
        if int(char) in can_use:
            ans += char
        else:
            for z in range(int(char)+1, 10):
                if z in can_use:
                    ans += str(z)
                    for rem in range(i+1, len(digits)):
                        ans += str(can_use[0])
                    print(ans)
                    exit()

            ok = True

            for i in range(len(ans)-1, -1, -1):
                for j in range(int(ans[i])+1, 10):
                   if j in can_use:
                       ans = str(j)
                       for k in range(1, len(digits)):
                           ans += str(can_use[0])

                       print(ans)
                       flag = True
                       break
                if flag:
                    break
        if flag:
            break

    if not flag:
        ans = ""
        if ok:
            for i, char in enumerate(digits):
                if i == 0 and can_use[0] == 0:
                    ans += str(can_use[1])
                else:
                    ans += str(can_use[0])
            ans += str(can_use[0])
            print(ans)
        else:
            for i, char in enumerate(digits):
                if int(char) in can_use:
                    ans += char

            print(ans)
