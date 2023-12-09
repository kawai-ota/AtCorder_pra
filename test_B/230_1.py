s = input()
t = 'oxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxxoxx'

for i in range(len(t)):
   if t[i:i + len(s)] == s:
       print("Yes")
       exit()
print("No")