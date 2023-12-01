s = input()

first_num = s.find("A")
second_num = s.rfind("Z")

ans_index = abs(first_num + second_num) + 1
print(ans_index)