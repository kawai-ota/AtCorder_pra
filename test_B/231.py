from collections import Counter
n = int(input())
ans = []

for _ in range(n):
    s = input()
    ans.append(s)

count_elements = Counter(ans)

max_elements = count_elements.most_common(1)[0][0]

print(max_elements)