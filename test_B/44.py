s = input()

char_count = {}

for char in s:
   char_count[char] = char_count.get(char,0) + 1

for count in char_count.values():
  if count % 2 != 0:
    print("No")
    exit()
else:
  print("Yes")