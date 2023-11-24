def solution(nums):
    n = len(nums)
    result = []

    for i in range(n):
        left_max_count = 1
        left = i - 1
        while left >= 0 and nums[left] < nums[i]:
            left_max_count += 1
            left -= 1

        right_max_count = 1
        right = i + 1
        while right < n and nums[right] < nums[i]:
            right_max_count += 1
            right += 1

        total_count = left_max_count + right_max_count - 1
        result.append(total_count)

    return result