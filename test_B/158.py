s = input()
n = len(s)
mid = n // 2

if s == s[::-1]:
  if s[:mid] == s[:mid][::-1] and s[mid + 1:] == s[mid + 1:][::-1]:
     print("Yes")
  else:
     print("No")
else:
      print("No")