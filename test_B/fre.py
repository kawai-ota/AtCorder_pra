def merge_intervals(interval1, interval2):
    return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

def solution(intervals):
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []

    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = merge_intervals(merged_intervals[-1], interval)

    return merged_intervals