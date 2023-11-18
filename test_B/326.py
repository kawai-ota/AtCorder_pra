n = int(input())

while True:
  hundreds = n // 100
  tens = (n // 10) % 10
  ones = n % 10
  
  if (hundreds * tens == ones):
    print(n)
    break
  
  n += 1