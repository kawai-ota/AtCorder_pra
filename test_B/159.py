n, a, b = map(int, input().split())

blue_balls = (n //(a + b)) * a

if n % (a + b) > a:
   blue_balls += a
else:
   blue_balls += n % (a + b)

print(blue_balls)