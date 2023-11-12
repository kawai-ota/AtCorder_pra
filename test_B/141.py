s = input()

ans_1 = True
ans_2 = True

for i in range(len(s)):
   if i % 2 == 0 and s[i] not in 'RUD':
      ans_1 = False
   elif i % 2 != 0 and s[i] not in 'LUD':
      ans_2 = False

if ans_1 and ans_2:
   print("Yes")
else:
   print("No")