l, r = map(int, input().split())
s = input()

str_1 = s[:l - 1]
str_2 = s[l - 1:r]
str_3 = s[r:]

str_4 = str_2[::-1]

ans = str_1 + str_4 + str_3
print(ans)