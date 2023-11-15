a = input()
b = input()
c = input()

d = [a,b,c]
if "ABC" not in d:
  print("ABC")
elif "ARC" not in d:
  print("ARC")
elif "AGC" not in d:
  print("AGC")
else:
  print("AHC")