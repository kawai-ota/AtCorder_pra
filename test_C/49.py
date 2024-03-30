T = input()
if T.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "") == "":
    print("YES")
else:
    print("NO")