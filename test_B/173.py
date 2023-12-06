n = int(input())
ac_sum = 0
wa_sum = 0
tle_sum = 0
re_sum = 0

for i in range(n):
    s = input()
    if s == "AC":
        ac_sum += 1
    elif s == "WA":
        wa_sum += 1
    elif s == "TLE":
        tle_sum += 1
    elif s == "RE":
        re_sum += 1

print(f"AC x {ac_sum}")
print(f"WA x {wa_sum}")
print(f"TLE x {tle_sum}")
print(f"RE x {re_sum}")
