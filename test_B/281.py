s = input()

if len(s) == 8 and s[0].isUpper() and s[-1].isUpper():
   substrings = s[1:7]
   if substrings.isdigit() and 100000 <= int(substrings) <= 999999:
      print("Yes")
   else:
      print("No")
else:
    print("No")