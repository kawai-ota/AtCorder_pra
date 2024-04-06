from collections import Counter
N = int(input())
numbers = [int(input()) for _ in range(N)]
count_numbers = Counter(numbers)
odd_count = sum(1 for count in count_numbers.values() if count % 2 == 1)
print(odd_count)
