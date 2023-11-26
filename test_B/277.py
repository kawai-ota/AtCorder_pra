n = int(input())
first = ["H","D","C","S"]
second = ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
ans1 = True
strings = set()

for i in range(n):
    s = input()
    if s[0] in first and s[1] in second and s not in strings:
        strings.add(s)
    else:
        ans1 = False
    
if ans1 and len(strings) == n:
    print("Yes")
else:
    print("No")