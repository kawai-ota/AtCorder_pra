A, B, C, X, Y = map(int, input().split())
price = 0
if A+B <= 2*C:
	price += A*X + B*Y
else:
	min_AB = min(X, Y)
	price += 2 * C * min_AB
	if X > Y:
		price += min(A, 2 * C) * (X - min_AB)
	else:
		price += min(B, 2 * C) * (Y - min_AB)
print(price)