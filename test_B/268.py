s = input()
t = input()

sl = len(s)
tl = len(t)

if (sl <= tl):
   if s == t[0:sl]:
      print("Yes")
   else:
      print("No")
else:
    print("No")