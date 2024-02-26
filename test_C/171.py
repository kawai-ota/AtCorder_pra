n = int(input())
base = ord('a')

index = []
while n >= 1:
  n -= 1
  index.append(n % 26)
  n //= 26

ans = ""
index = index[::-1]
for i in index:
  ans += chr(base + i)
print(ans)