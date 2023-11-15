x = int(input())

yen_500 = x // 500
x = x - (yen_500 * 1000)
happiness = yen_500 * 1000

happiness = happiness + (x // 5) * 5

print(happiness)