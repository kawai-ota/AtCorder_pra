r,c = map(int,input().split())

if max(abs(r - 8),abs(c - 8)) % 2 == 0:
   print('white')
else:
   print('black')