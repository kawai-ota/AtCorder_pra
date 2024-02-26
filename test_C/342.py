from collections import defaultdict
n = int(input())
s = input()
q = int(input())
cd = [input().split() for _ in range(q)]
# c = defaultdict(list)
# for i in range(n):
#     c[s[i]].append(i)
dic = {chr(i): [chr(i)] for i in range(ord('a'), ord('z')+1)}
for c, d in cd:
    if dic[c] and c != d:
        if not dic[d]:
            dic[d] = dic[c]
        else:
            dic[d] += dic[c]
        dic[c] = []
rev = dict()
for i in dic:
    for j in dic[i]:
        rev[j] = i
for si in s:
    print(rev[si], end='')
